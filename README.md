### Kirill Baravoy

#### Home task: 04

<dl>
  <dt>Requirements:</dt>
  <dd>install python environment : 3.0.0 +</dd>
  <dd>install git</dd>
</dl>

**_How to use script_** <br>
1) git clone https://github.com/borovoykirill/devops_lab.git
2) cd devops_lab
3) checkout -b homework4
4) chmod +x pr-stats
5) ./pr-stats *-some-key*. Be careful, after starting the script, he will ask you to enter 
your username on the github and password.  

For example:
Input: ./pr-stats -owner alenaPy -repo devops_lab -number 12 -status -created -label -basic -user -comments -commit*
Output:
Title of pull request: Homework1: Vitali Andrushkevich
Source of pull request: Vitalyazavr/devops_lab
Pull request status: open
Created: 2020-02-28T14:22:17Z
Updated: 2020-03-02T16:40:24Z
Merged: None
Closed: None
Number of comments created: 0
Number of commits created: 1
User who opened pull request: Vitalyazavr
Attached labels: accepted

__N.B. To clarify information which keys can be used, please type ./pr-stats -h__ 
optional arguments:
  -h, --help      show this help message and exit
  -version        Application version
  -owner OWNER    <repository owner>
  -repo REPO      <repository name>
  -number NUMBER  <pull request number>
  -status         Pull request status
  -basic          Basic statistics about merged/closed rate.
  -created        Date of creating pull request and updated
  -comments       Number of comments created
  -commits        Number of commits created
  -user           User who opened pull request
  -label          Attached labels
