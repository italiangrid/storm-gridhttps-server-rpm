%define _sysconfdir /etc
%define _javadir /usr/share/java
%define _docdir /usr/share/doc
%define default_user root

%define maven_repository ${MavenLocalRepository}
%define maven_settings ${MavenSettings}
%define maven_profile ${MavenProfile}
%define conf_dir ${ConfDir}
%define short_name ${ModuleName}
%define log_dir ${LogDir}
%define work_dir ${WorkDir} 

Summary: The StoRM GridHTTPS component
Name: ${PackageName}
Version: ${PackageVersion}
Release: ${PackageRelease}%{?dist}
License: Apache License 2.0
Vendor: EMI
URL: http://storm.forge.cnaf.infn.it
Group: Application/Internet
Packager: Michele Dibenedetto storm-support@lists.infn.it

BuildArch: noarch
BuildRequires: maven
BuildRequires: java-1.6.0-openjdk-devel

Requires: java-1.6.0-openjdk

BuildRoot: %{_builddir}/%{name}-root
AutoReqProv: yes
Source: %{name}-%{version}.tar.gz

%description
The StoRM GridHTTPS component providing plain http(s) access and WebDAV access to StoRM managed files

%prep


%setup -c

%build
mvn %{maven_settings} %{maven_repository} -U -Dmaven.test.skip=true -P %{maven_profile} install

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT
test -d assembler/target/%{name}-fakeroot.dir && cp -vR assembler/target/%{name}-fakeroot.dir/* $RPM_BUILD_ROOT

%clean

%post
#during an install, the value of the argument passed in is 1
#during an upgrade, the value of the argument passed in is 2
##if [ "$1" = "1" ] ; then
if [ "$1" = "2" ] ; then
  
  rpm -q tomcat5 &> /dev/null
  test $? -eq 0 && TOMCAT_PACKAGE_NAME="tomcat5" && TOMCAT_COMMON_LIB_DIR="common/lib" && TOMCAT_SERVER_LIB_DIR="server/lib" && TOMCAT_CONF_LOGGING_DIR="common/classes"
  rpm -q tomcat6 &> /dev/null
  test $? -eq 0 && TOMCAT_PACKAGE_NAME="tomcat6" && TOMCAT_COMMON_LIB_DIR="lib" && TOMCAT_SERVER_LIB_DIR="lib" && TOMCAT_CONF_LOGGING_DIR="lib"
  if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/gridhttps_common.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/gridhttps_common.jar ;
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/gridhttps_filter.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/gridhttps_filter.jar ;
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/httpclient.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/httpclient.jar ;
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/httpcore.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/httpcore.jar ;
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/commons-codec.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/commons-codec.jar ;
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/commons-modeler.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/commons-modeler.jar  ;
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_SERVER_LIB_DIR}/*commons-modeler*.jar.storm.saved ] ; then
		VAR=`ls /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_SERVER_LIB_DIR}/*commons-modeler*.jar.storm.saved`
		LENGTH=`expr length "$VAR"`
		LENGTH=$(($LENGTH - 12))
		NEW_NAME=`echo $VAR | head -c $LENGTH`
		mv /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_SERVER_LIB_DIR}/*commons-modeler*.jar.storm.saved  $NEW_NAME;
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/*commons-modeler*.jar.storm.saved ] ; then
		VAR=`ls /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/*commons-modeler*.jar.storm.saved`
		LENGTH=`expr length "$VAR"`
		LENGTH=$(($LENGTH - 12))
		NEW_NAME=`echo $VAR | head -c $LENGTH`
		mv /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/*commons-modeler*.jar.storm.saved  $NEW_NAME;
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/trustmanager.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/trustmanager.jar
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_SERVER_LIB_DIR}/trustmanager-tomcat.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_SERVER_LIB_DIR}/trustmanager-tomcat.jar
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/vomsjapi.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/vomsjapi.jar
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/[bcprov].jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/[bcprov].jar
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/log4j.jar ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_COMMON_LIB_DIR}/log4j.jar
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/conf/log4j-trustmanager.properties ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/conf/log4j-trustmanager.properties
	fi
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_CONF_LOGGING_DIR}/log4j.properties ] ; then
		DEST_FILE=`readlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_CONF_LOGGING_DIR}/log4j.properties`
		if [ $? -eq 0 ] ; then
			if [ $DEST_FILE="${conf_dir}/${short_name}/log4j-tomcat.properties" ] ; then
				unlink /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_CONF_LOGGING_DIR}/log4j.properties
			fi
		else
			echo "Error. Unable to read link at /usr/share/${TOMCAT_PACKAGE_NAME}/${TOMCAT_CONF_LOGGING_DIR}/log4j.properties"
		fi
	fi
	
	
	# Remove log files
	rm -f /var/log/storm/velocity-gridhttps*
	
	# Remove tomcat context files
	rm -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/Catalina/localhost/storageArea* 
	
	# Clean yaim stuff
	
	# Delete the link to web.xml generated file 
	if [ -f /etc/${TOMCAT_PACKAGE_NAME}/${TOMCAT_PACKAGE_NAME}.conf ] ; then
		# tomcat is still installed. Put back its original configuration file
		if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml -a -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml.storm.saved ] ; then
			unlink /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml
			mv /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml.storm.saved /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml
		fi
		if [ -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml -a -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml.storm.saved ] ; then
			rm -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml
			mv /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml.storm.saved /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml
		fi
	else
		# tomcat has been removed. Remove the created configuration files 
		if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml ] ; then
			unlink /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml
		fi
		if [ -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml.storm.saved ] ; then
			rm -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/web.xml.storm.saved
		fi
		if [ -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml ] ; then
			rm -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml
		fi
		if [ -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml.storm.saved ] ; then
			rm -f /usr/share/${TOMCAT_PACKAGE_NAME}/conf/server.xml.storm.saved 
		fi
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/conf/log4j-trustmanager.properties ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/conf/log4j-trustmanager.properties
	fi
	
	# Delete the web.xml file produced by yaim (not owned by the rpm)
	if [ -f ${conf_dir}/${short_name}/web.xml ] ; then
		rm -f ${conf_dir}/${short_name}/web.xml
	fi
	
	ls ${conf_dir}/${short_name}/web.xml.bkp_* &> /dev/null
	if [ $? -eq 0 ]; then
		rm -f ${conf_dir}/${short_name}/web.xml.bkp_*
	fi
	
	if [ -L /usr/share/${TOMCAT_PACKAGE_NAME}/webapps/gridhttps.war ] ; then
		unlink /usr/share/${TOMCAT_PACKAGE_NAME}/webapps/gridhttps.war ;
	fi
	
fi

%preun
#during an upgrade, the value of the argument passed in is 1
#during an uninstall, the value of the argument passed in is 0
if [ "$1" = "0" ] ; then
   if [ -f %{conf_dir}/%{short_name}/server.ini ]; then
      rm -f %{conf_dir}/%{short_name}/server.ini    
   fi
   ls %{conf_dir}/%{short_name}/server.ini.bkp_* &> /dev/null
   if [ $? -eq 0 ]; then
      rm -f %{conf_dir}/%{short_name}/server.ini.bkp_*
   fi 
#elif [ "$1" = "1" ] ; then
fi                                                           

%files
%defattr(-,%{default_user},%{default_user})
%dir %{conf_dir}/
%dir %{conf_dir}/%{short_name}/
%config %{conf_dir}/%{short_name}/logback.xml
%attr(640,root,root) %config %{conf_dir}/%{short_name}/server.ini.template
%attr(755,%{default_user},%{default_user}) %{_sysconfdir}/init.d/%{name}

%dir %{_docdir}/%{name}-%{version}
%{_docdir}/%{name}-%{version}/LICENSE.txt

%dir %{_javadir}/%{name}                             
%{_javadir}/%{name}/server.jar
%{_javadir}/%{name}/webapp.war
%{_javadir}/%{name}/storagearea.jar

%attr(770,%{default_user},%{default_user}) %dir %{work_dir} 
%attr(774,%{default_user},%{default_user}) %dir %{log_dir} 

%changelog
* Fri Feb 23 2011 <Michele Dibenedetto> <michele.dibenedetto@cnaf.infn.it> %{version}-%{release}
-the storm-gridhtps-server is responsible provide http(s) access to files 
-the service verifies https calls by unspecting the received certificate and eventualy its VOMS extensions
-it interacts with storm-gridhttps-server using the Authorization Rest interfacethat it provides. Current version is compliant with storm-backend-server Authorization rest interface version 1.0.0
