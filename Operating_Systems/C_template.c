#include <stdio.h> //basic c library

void my_function() { //declares function
  printf("This is a function\n"); //prints a string
}

int main(void) { //main function
  printf("Hello World\n"); //print string, \n is for new line
  printf("%i\n",5); //print an integer, can use %d too
  printf("%f\n",5.5); //print a double, can use %lf too
  printf("%c\n",'A'); //print a char
  int var = 0; //declare variable var as an int and initialize it as 0
  FILE *my_file; //declare my_file as a file
  //for fopen, r opens for reading, w opens for writing or creates a file, a opens for appending file or creates a file, r+ opens for both reading and writing, w+ opens for both reading and writing but zeros out the file first of creates a file, a+ opens for both reading and writing but writing can only be appended or creates a file.
  my_file = fopen("file.txt","w"); //open or creates file.txt with writing access
  fputs("This is a string\n",my_file); //writes to my_file
  fprintf(my_file,"This is a second string\n"); //also writes to my_file
  fprintf(my_file,"Here is a number:%d\n",22); //writes an int to my_file
  fclose(my_file); //closes file
  my_file = fopen("file.txt","a"); //open file.txt with appending access
  fputs("Another line at the end\n",my_file);
  fclose(my_file);
  my_file = fopen("file.txt","r"); //open file.txt with reading access
  char c; //declares a variable c as a char
  while((c = fgetc(my_file))!=EOF) { //while loop that loops untile fgetc is EOF
    printf("%c",c); //prints c
  } //end of while loop
  for (int i = 10;i > 0; i--) { //for loop with decrementing int
    printf("%i\n",i); //printing i
  } //end of for loop
  if (2 == 3) { //if statement 2 = 3
    printf("2 = 3\n"); //print 2 = 3
  } //end if
  else if (2 > 3) { //else if statement 2 > 3
    printf("2 > 3\n"); //print 2 > 3
  } //end else if
  else { //else statement
    printf("2 < 3\n"); //print 2 < 3
  } //end else
  my_function(); //calls my_function
  return 0; //return at end signifying that program completed successfully
}
