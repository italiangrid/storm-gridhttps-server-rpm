StoRM-GridHTTPs-Server-rpm
==========================

StoRM GridHTTPs Server exposes a standard WebDAV interface on top of StoRM BackEnd Service to 
provide WebDAV access to a Grid Storage Element. This component behaves also as a pure HTTP(s) transfer 
server when used in conjunction with StoRM SRM interface.
The storm-gridhttps-server-rpm component is used to build StoRM GridHTTPs Server source code (from version 2.0.0).

## Building
Required packages:

* git
* maven

Build commands:
<pre>
git clone https://github.com/enricovianello/storm-gridhttps-server-rpm.git
cd storm-gridhttps-server-rpm.git
make all
</pre>

If you want to build a different branch of storm-gridhttps-server launch make specifying that branch as value for tag variable:
<pre>
make tag=<branch-name> all
</pre>

## Contact info

If you have problems, questions, ideas or suggestions, please contact us at
the following URLs

* GGUS (official support channel): http://www.ggus.eu
