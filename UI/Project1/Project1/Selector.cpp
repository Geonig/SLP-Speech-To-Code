#include <iostream>
#include <windows.h>
using namespace std;

static BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam);

static BOOL CALLBACK EnumWindowsProc(HWND hwnd, LPARAM lParam)
{

	char class_name[80];
	char title[80];
	GetClassName(hwnd, class_name, sizeof(class_name));
	GetWindowText(hwnd, title, sizeof(title));
	printf("Window title: %c\n" , title);
	cout << "Class name: " << class_name << endl << endl;


	return TRUE;
}