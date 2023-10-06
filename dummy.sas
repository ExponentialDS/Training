LIBNAME mydata 'C:/path/to/sas7bdat/files';
DATA mydata.dummy;
    INPUT ID 3. Name $12.;
    DATALINES4;
1 'Alice';
2 'Bob';
3 'Charlie';
4 'David';
5 'Eve';

;;;;
RUN;
