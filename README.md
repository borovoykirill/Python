### Kirill Baravoy

#### Home task: 04

<dl>
  <dt>Requirements:</dt>
  <dd>install python environment : 3.0.0 +</dd>
  <dd>install git</dd>
</dl>

**_Description of script_** <br>
This script is used to get information about pool request.<br>

**_How to use script_** <br>
1) git clone https://github.com/borovoykirill/devops_lab.git<br>
2) cd devops_lab<br>
3) checkout -b homework4<br>
4) chmod +x pr-stats<br>
5) ./pr-stats *-some-key*. Be careful, after starting the script, he will ask you to enter<br> 
your username on the github and password.<br>  

For example:<br>
Input: __*./pr-stats -owner alenaPy -repo devops_lab -number 12 -status -created -label -basic -user -comments -commit*__<br>
Output:<br>
Title of pull request: Homework1: Vitali Andrushkevich<br>
Source of pull request: Vitalyazavr/devops_lab<br>
Pull request status: open<br>
Created: 2020-02-28T14:22:17Z<br>
Updated: 2020-03-02T16:40:24Z<br>
Merged: None<br>
Closed: None<br>
Number of comments created: 0<br>
Number of commits created: 1<br>
User who opened pull request: Vitalyazavr<br>
Attached labels: accepted<br>

__N.B. To clarify information which keys can be used, please type *./pr-stats* -h__<br> 
optional arguments:<br>
  -h, --help      show this help message and exit<br>
  -version        Application version<br>
  -owner OWNER    <repository owner><br>
  -repo REPO      <repository name><br>
  -number NUMBER  <pull request number><br>
  -status         Pull request status<br>
  -basic          Basic statistics about merged/closed rate.<br>
  -created        Date of creating pull request and updated<br>
  -comments       Number of comments created<br>
  -commits        Number of commits created<br>
  -user           User who opened pull request<br>
  -label          Attached labels<br>
