1.- 
A)
Added line 167 to Rio_writen(fd, buf, filesize);
Why? to repopulate back to the client.
Why that line instead of other lines?
I CTR+F for header. I tested adding writen in every line.

B) HTTP/1.0 200 OK Server:Tiny Web Server Content-length:99 Content-type: text/html

C) HTTP/2


2.- Added lines 182 - 183.
Looked for an image or html tag. Added the video tag in.

3.- Added line 162-163.
CTR+F for mmap. There was only one, so I deleted it and wrote what was asked for.
srcp was replaced for malloc of filesize
rio_readn would read the current files position of descriptor srcfd
Did try many malloc(data) and rio_readn(stuff), but the rio_writen was returning bad address.
Trial and error.