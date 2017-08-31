#include <cs50.h>
#include <stdio.h>

int main(void)
{
    printf("name: ");
    string s = get_string();
    printf("hello, %s\n", s);
}