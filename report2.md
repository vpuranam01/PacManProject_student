Report:

Pranav Khatri
- Created report.md file
- Renamed Player to Pacman using the following commands:

grep -rIl "player" . | xargs sed -i '' 's/player/pacman/g'

grep -rIl "Player" . | xargs sed -i '' 's/Player/Pacman/g'

Used grep and sed commands. We have two commands because one of them 
is for lowercase "player" while the other command is for uppercase "Player".


Akhilesh Puranam



Kamran Mair



Rahul Anantuni


