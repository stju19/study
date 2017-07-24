#! /bin/bash

git config user.name "10183988"
git config user.email "ju.guanqiu@zte.com.cn"

git config alias.co checkout
git config alias.ci commit
git config alias.br branch
git config alias.st status
git config alias.ps "push origin HEAD:refs/for/master"
git config alias.lg "log --color --graph --pretty=format:'%Cred%h%Creset -%C(yellow)%d%Creset %s %Cgreen(%cr) %C(bold blue)<%an>%Creset' --abbrev-commit --all"
git config alias.last 'log -1'
git config alias.unstage 'reset HEAD'

git config diff.tool vimdiff
git config difftool.prompt false
git config alias.vimdiff difftool

git config core.filemode true
git config core.autocrlf false
git config color.ui true