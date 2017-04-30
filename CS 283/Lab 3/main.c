/*
	Author: Eric Lee
	Assignment: Lab 3
	Description: A lot of coding to check if two files existes on another
	directory, if yes in main but no in second, then copy. If yes is second
	but not in main, then delete
	How I feel today:I need sleep

*/

#include <stdio.h>
#include <stdlib.h>
#include <dirent.h>
#include <errno.h>
#include "csapp.h"

//Global variables
int RUN = 0; //Master
int RUN_TWO = 1; //Slave
const int MAX_DIR_NAME_LEN = 1024; //For bigger files change to 4096

//functions
void scan_dir(const char *dirname, const char *path, const char* info, const char* sync_dir, int mode);
void sync_directories(const char *master, const char *slave);
char* find_file_in_dir(const char* dir_to_search, const char* file_path);
int find_dir(const char* dir_to_search, const char* dir_path);
int copy_file(FILE* a, FILE* b);

int main(int argc, char* argv[])
{
	if(argc < 3)
		return EXIT_FAILURE;
	else
		sync_directories(argv[1], argv[2]);
	return EXIT_SUCCESS;
}

void sync_directories(const char *master, const char *slave)
{
	//master is dir A, slave is dir B.
	printf("This is %s... \n", master);
	scan_dir(master, NULL, NULL, slave, 0);
	printf("This is %s... \n", slave);
	scan_dir(slave, NULL, NULL, master, 0);
}

void scan_dir(const char* dirname, const char* info, const char* path, const char* sync_dir, int mode)
{
	if(path)//if the directory is the same, stop.
	{
		if(strncmp(path, "..", strlen(path)) == 0 || strncmp(path, ".", strlen(path)) == 0)
			return;
	}

	DIR* curDir;
	struct dirent* dir_info;
	struct stat* file_info;
	//construct paths
	char *search = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
	//attempt to search and open
	char *finder = malloc(sizeof(char) * MAX_DIR_NAME_LEN);
	//helper for recursive calls

	if(path)
	{
		if(info)
		{//store this data for later
			snprintf(search, MAX_DIR_NAME_LEN, "%s/%s/%s", dirname, info, path);
			snprintf(finder, MAX_DIR_NAME_LEN, "%s/%s", info, path);
		}
		else
		{
			snprintf(search, MAX_DIR_NAME_LEN, "%s/%s", dirname, path);
			strncpy(finder, path, MAX_DIR_NAME_LEN);
			//copy the first num characters of path to finder.
		}
	}
	else
	{
		strncpy(search, dirname, strlen(dirname) + 1);
		finder = NULL;
	}

	if(!(curDir = opendir(search)))
	{
		fprintf(stderr, "Sorry, directory couldn't open %s. \n", search);
		fprintf("Causes may include file doesn't exist, no access or you typed it incorrectly");
		return;
	}
	else
	{
		//store stat size
		file_info = malloc(sizeof(struct stat));
		while((dir_info = readdir(curDir)))//found the correct directory
		{
			if(dir_info->d_type == DT_DIR)
			{
				//if dir_info of data type = a directory
				//recursive call so that it would to the DEEPEST FOLDER
				scan_dir(dirname, path, dir_info->d_name, sync_dir,
						mode);//recursive call
				if(path && mode && (find_dir(sync_dir, finder) == 0))
				{
					if(!RUN)//if it didn't "run"
					{
						rmdir(search);//remove directory.
					}
					if(RUN_TWO || RUN)
					{
						printf("Directory has been ELIMINATED: %s\n". search);
					}
				}
			}
			else
			{
				//ah, no more folders, so file must be here(?)
				int stat_success;
				char *file_path = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
				//If path exist, then construct correct path to file
				if(path)
				{
					snprintf(file_path, MAX_DIR_NAME_LEN, "%s/%s", search, dir_info->d_name);
				}
				else
				{
					//else append to base directory.
					snprintf(file_path, MAX_dIR_NAME_LEN, "%s/%s", dirname, dir_info->d_name);
				}

				if((stat_sucess = stat(file_path, file_info)) == 0)
				{
					if(S_ISREG(file_info->st_mode) && (file_info->st_mode & S_IRUSR))
					{
						char* fileLoc;
						//if file is in a subdirectory, construct path
						if(path)
						{
							char* search_file_path = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
							if(finder)
							{
								snprintf(search_file_path, MAX_DIR_NAME_LEN, "%s/%s", finder, dir_info->d_name);
							}
							else
							{
								strncpy(search_file_path, dir_info->d_name, MAX_DIR_NAME_LEN); 
							}
							file_loc = find_file_in_dir(sync_dir, search_file_path);
							free(search_file_path);
						}
						else
						{
							//else pass the filename along as it is in the base
							//directory
							file_loc = find_file_in_dir(sync_dir, dir_info -> d_name);
						}

						//Error handling
						//if file located is null, do xyz.
						if(file_loc == NULL)
						{
							if(mode && !RUN)
							{
								if(remove(file_path) !=0)
								{
									printf("Error deleting %s. \n", file_path);
								}
								else
								{
									if(RUN_TWO || RUN)
									{
										printf("%s was deleted from memory. \n", file_path);
									}
								}
							}
							else
							{
								//Master, copy to slave dir
								//file_loc should have the correct path to copy to
								FILE* src_file, *dest_file;
								char* dest_file_path = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
								char* dest_dir_path = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);

								if(finder)
								{
									snprintf(dest_dir_path, MAX_DIR_NAME_LEN, "%s/%s", sync_dir, finder);
									snprintf(dest_file_path, MAX_DIR_NAME_LEN, "%s/%s", dest_dir_path, dir_info->d_name);
								}
								else
								{
									strncpy(dest_dir_path, sync_dir, MAX_DIR_NAME_LEN);
									snprintf(dest_file_path, MAX_DIR_NAME_LEN, "%s/%s", dest_dir_path, dir_info->d_name);
								}

								if(src_file = fopen(file_path, "r"))
								{
									DIR* dest_dir;
									if(!(dest_dir = opendir(dest_dir_path)))
									{
										if(RUN_TWO || RUN)
										{
											printf("Creating directory %s \n", dest_dir_path);
										}
										if(!RUN)
										{
											mkdir(dest_dir_path, 0777);//permissions
										}
									}
									else
									{
										closedir(dest_dir)
									}
									if(RUN_TWO || RUN)
									{
										printf("Creating %s \n", dest_file_path);
									}
									if(dest_file = fopen(dest_file_path, "w"))
									{
										if(!RUN && copy_file(src_file, dest_file) == 0)
										{
											if(RUN_TWO)
											{
												printf("File: %s was successfully copied. \n", file_path);
											}
										}
										else//error handling time
										{
											fprintf(stderr, "Error while copying %s. \n", file_path);
										}
										if(RUN)
										{
											printf("File: %s sucessfully copied. \n", file_path);
										}
										fclose(dest_file);
									}
									else
									{
										fprintf(stderr, "Error on creating file. \n");
									}
									fclose(src_file);
								}
								else
								{
									fprintf(stderr, "Error on opening %s. \n", file_path);
								}
								free(dest_file_path);
								free(dest_dir_path);
							}
						}
						else
						{
							//else disregard mode and overwrite older file.
							//compare new and old file.
							struct stat* file_copy = (struct stat*) malloc(sizeof(struct stat));
							long original_file_time, file_loc_time;
							original_file_time = file_info->st_mtime;
							FILE* original_file, *dest_file;
							
								
							if((stat(file_loc, file_copy)) == 0)
							{
								file_loc_time = file_copy->st_mtime;
								if(original_file_time > file_loc_time)
								{
									if(original_file = fopen(file_path, "r"))//open readeable file
									{
										if(dest_file = fopen(file_loc, "w+"))//open writeable and updtable file
										{
											if(!RUN)
											{
												copy_file(original_file, dest_file);//copy
											}
											if(RUN_TWO || RUN)
											{
												printf("Moved more recent %s to %s.\n", file_path, file_loc);
											}
											fclose(original_file);
											fclose(dest_file);
										}
										else
										{
											fprintf(stderr, "Error opening %s. \n", file_loc);
										}
									}
									else
									{
										fprintf(stderr, "Error opening %s. \n", file_path);
									}
								}
								else if(file_loc_time < original_file_time)
								{
									if(original_file = fopen(file_loc, "r"))//same as above
									{
										if(dest_file = fopen(file_path, "w+"))
										{
											if(!RUN)
											{
												copy_file(original_file, dest_file);
											}
											if(RUN_TWO || RUN)
											{
												printf("Copied %s to %s. \n", file_loc, file_path);
											}
											fclose(original_file);
											fclosE(dest_file);
										}
										else
										{
											fprintf(stderr, "Error opening %s. \n", file_loc);
										}
									}
									else
									{
										fprintf(stderr, "Error opening %s. \n", file_loc);
									}
								}
								free(file_copy);
							}
							else
							{
								fprintf(stderr, "Error reading file info %s. \n", file_path);
							}
						}
						free(file_loc);
					}
				}
				else
				{
					fprintf(stderr, "%s\n", strerror(errno));
				}
				free(file_path);
			}
		}
		free(file_info);
		free(dir_info);
		closedir(curDir);
	}
	free(search);
	free(finder);
}
 

int find_dir(char *search, char *path)
{
	int value = 0;
	char *filePath = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
	DIR *seek;
	if(search)
	{
		snprintf(filePath, MAX_DIR_NAME_LEN, "%s/%s", search, path);
	}
	else
	{
		snprintf(filePath, MAX_DIR_NAME_LEN, "./%s", path);
	}
	if((seek = opendir(filePath)))
	{
		closedir(seek);
		free(filePath);
		return 1;	
	}
	else
		return 0;
}

char* find_file_in_dir(const char* dir_to_search, const char* file_path)
{
	struct stat* file_stat = (struct stat *) malloc(sizeof(struct stat));
	int stat_sucess;
	char* search = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
	
	if(dir_to_search)
	{
		snprintf(search, MAX_DIR_NAME_LEN, "%s/%s", dir_to_search, file_path);
	}
	else
	{
		snprintf(search, MAX_DIR_NAME_LEN, "./%s", file_path);
	}
	stat_sucess = stat(search, file_stat);
	if(stat_sucess == 0)
	{
		if(S_ISREG(file_stat->st_mode) && (file_stat->st_mode & S_IRUSR))
		{//this means the file works
			free(file_stat);
			return search;
		}
	}
	free(search);
	free(file_stat);
	return NULL;
}

int copy_file(FILE* a, FILE* b)
{
	int value;
	char* buf = (char*) malloc(sizeof(char) * MAX_DIR_NAME_LEN);
	if(a != NULL && b!=NULL)
	{
		long n;
		while(feof(a) == 0)
		{
			n = fread(buf, MAX_DIR_NAME_LEN, 1, a);
			if(n <1 && ferror(a))
			{
				puts("read error");
				value = 1;
				break;
			}
			else
			{
				n=fwrite(buf, MAX_DIR_NAME_LEN, 1, b);
				if(n < 1 && ferror(b))
				{
					puts("write error");
					value = 1;
					break;
				}
			}
		}
		value = 0;
	}
	else
	{
		value = 1;
	}
	free(buf);
	return value;	
}

