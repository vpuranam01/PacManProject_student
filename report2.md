Report:

Pranav Khatri
- Created report.md file
- Reviewed PR for CI/CD Pipeline
- Renamed Player to Pacman using the following commands:

grep -rIl "player" . | xargs sed -i '' 's/player/pacman/g'

grep -rIl "Player" . | xargs sed -i '' 's/Player/Pacman/g'

Used grep and sed commands. We have two commands because one of them 
is for lowercase "player" while the other command is for uppercase "Player".


Akhilesh Puranam
- Created CI/CD Pipeline
- Reviewed PR for Secure Sensitive Information
- Reviewd PR for report and resolved merge conflicts

Kamran Mair
- Worked on securing sensitive information


Rahul Anantuni
- Worked on securing sensitive information
- Reviewed PR for Renaming

