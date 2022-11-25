# Agenda

* Piping and Redirection
* searching 
	- text inside text/file
	- file inside filesystem
* process managment
* links
* shell scripting
	- variables
	- expressions
	- if
	- loops (while, for)
	

# Piping and Redirection

## Redirection
* File streams: stdin=0 , stdout=1 , stderr=2
* redireection for any file stream:
	- input redirection:  `./program  <input_file.txt` -> this redirects the input stream to take its input from a file named `input_file.txt`
	- output redirection: `./program > output_file.txt` -> this redirects the output stream to a file named `output_file.txt`.
		+ `output_file.txt` holds the contents of only stdout(1)
		+ if `output_file.txt` does not exist its created from scratch
		+ if `output_file.txt` its overwritten with the new contents
		+ to append to `output_file.txt` use `>>` instead of '>'
	- Error redirection: `./program 2> error_log.txt` -> this redirects the contents of stderr stream to a file named `error_log.txt`
	
   NOTE: the default of the `>` operator is `1>` which is stdout, in order to redirect ONLY error use `2>` and redirect both to the same file `&>`
  

# Process Management



# user permissions

- root: admin prvilieges
- user: 
- group:



# Text processing utilities

## `cat`:
 concatenate the contents of two files.

## `tail`:
 prints the file from bottom to top 
 
## `head`:
 prints the file from top to bottom
 
## `grep` :
 general regualr expression print 
 	- n: print line numbers
 	- w: whole word search
 	- i: case insensitive
 	- r: recursive search in given directory
 	- I: ignore binary files
 	- A <integer> : print a number of <integer> lines After each search finding
 	- B <integer> : print a number of <integer> lines Before each search finding
 	- C <integer> : print a number of <integer> lines Before and After each search finding
 
## `cut` :
 - d "delimiter": delimiter string ->
 - f <field number>:
 
## `less`: 
 provides paginated output in terminal so that you can navigate large text output using arrow keys (UP-DOWN), ENTER , PG-UP,PG-DWN
 
# Network utilities:

## `ip`: 
   - a: print all network devices with their information
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
 	
