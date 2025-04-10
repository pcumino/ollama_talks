#!/bin/bash
#===========================================================#
#File Name:			run.sh
#Author:			Pedro Cumino
#Email:				pedro.cumino@av.it.pt
#Creation Date:		Sat 15 Feb 12:35:45 2025
#Last Modified:		Sat 15 Feb 12:35:47 2025
#Description:
#Args:
#Usage:
#===========================================================#

prompt="`cat prompt.txt | grep -vE "^$" | tail -n1 `"
echo "---" >> out.md
echo "##### [`date`]" >> out.md;
echo "**$prompt**" >> out.md;
# ollama run llama3 "Improve the following prompt: \"$prompt\"" >> out.md;
ollama run llama3 "\"$prompt\"" >> out.md;
echo "done!"