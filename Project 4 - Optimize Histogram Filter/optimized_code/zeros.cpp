#include "headers/zeros.h"

using namespace std;

vector < vector <float> > zeros(int height, int width) {
	//int i, j;
  
	// OPTIMIZATION: Reserve space in memory for vectors
	vector <float> newRow(width,0.0);
    vector < vector <float> > newGrid(height,newRow);
	

  	// OPTIMIZATION: nested for loop not needed
    // because every row in the matrix is exactly the same
	/*
    for (i=0; i<height; i++) {
		newRow.clear();
		for (j=0; j<width; j++) {
			newRow.push_back(0.0);
		}
		newGrid.push_back(newRow);
	}
    */
	return newGrid;
}