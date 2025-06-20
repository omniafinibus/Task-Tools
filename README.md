# Task-Tools
Scripts to maintain tasks in both .todo and .ics files

daily_notes looks at a directory which contains years and months of todo files, showing a history of when things where completed

task_csv_to_ics converts csv files with tasks into ics for uploading to your favorite calendar/task app

# Commands

## To Do files
```task_tools [DIR] update [-e] "nano" [-t] [-do]```

### Local 
```-t l```

### Daily
```-t d```

## Convert to ics
Supports both ```.todo``` and ```.csv```
```task_tools [DIR] toics [-e] "nano"```

## Convert to csv
Supports both ```.todo``` and ```.ics```
```task_tools [DIR] tocsv [-e] "nano"```
