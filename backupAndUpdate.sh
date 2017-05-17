#!/bin/env bash
# writer SY60216
# 脚本功能：版本的备份与更新 须1个目标版本参数(绝对路径)
# usage： 
#			bash backupAndUpdate.sh "/sourcePath/(filename|dirname)"

IFS=$' \t\n'
OLDPATH=$PATH
PATH=/bin:/usr/bin
export PATH

usage(){
        printf "usage:\n\t bash backupAndUpdate.sh '/sourcePath/(filename|dirname)'\n";
}

if [ $# != 1 ];then
	echo must have a source path argument!
	exit 2
fi
if [ "X$1" = "X-h" -o "X$1" = "X--help" ];then
	usage
	exit 3
fi
source=$1
iuser=$(whoami)
echo user is:$iuser
typeset -l mod;typeset -l pub;
modError1="";pubError1="";modfinish="";pubfinish="";modCheckOk="";pubCheckOk="";
modError2="";modError3="";modsum=0;pubsum=0;
pubError2="";pubError3=""

run(){
	# mod 和 pub 变量ok具体运行函数
	local list="5 4 3 2 1"
	echo waitting
	for s in $list
	do
		printf "***%s***" $s
		sleep 1s
		printf "\b\b\b\b\b\b\b"
	done
	echo beginning
	for m in $1
	do
		backupAndupdate_mod $m
		case $? in
			2)
				modError2=${modError2}","$m
				;;
			3)
				modError3=${modError3}","$m
				;;
			0)
				modfinish=${modfinish}","$m
				;;
		esac
	done
	backupAndupdate_pub $(echo $2)
}

mod_check(){
	# 检查mod是否正确
	if [ -d "/home/$iuser/innerapp/${1}" ];then
		return 0
	else
		return 1
	fi
}
pub_check(){
	#检查pub是否正确
	if [ -d "/home/$iuser/webhome/${1}" ];then
		return 0
	else
		return 1
	fi
}

backupAndupdate_mod(){
	#依据mod_lib文件夹备份和更新mod版本
	echo =======================${1}===============================
	local result=0
	echo start backup the module : $1
	mkdir -p /home/$iuser/backup/bak_$(date +%F)/$1
	find /home/$iuser/innerapp/ -name ${1}.jar | xargs -n1 -i -t mv -f {} /home/$iuser/backup/bak_$(date +%F)/${1}/ || result=2
	find /home/$iuser/innerapp/ -name ${1}_lib -type d | xargs -n1 -i -t mv -f {} /home/$iuser/backup/bak_$(date +%F)/${1}/ || result=2
	if [ $result -eq 0 ]
	then
		echo $1 backup success,now starting update...
		find /tmp/$(date +%m%d)/$dirname/ -name ${1}.jar -type f | xargs -n1 -i -t cp {} /home/$iuser/innerapp/${1}/ || result=3
		find /tmp/$(date +%m%d)/$dirname/ -name ${1}_lib -type d | xargs -n1 -i -t cp -r {} /home/$iuser/innerapp/${1}/ || result=3
		if [ $result -eq 0 ]
		then
			echo $1 update success!
		fi
	else
		echo $1 backup failed!
	fi
	return $result
}

backupAndupdate_pub(){
	#根据war包,备份与更新订阅号平台
	while test $# -gt 1
	do
		echo =======================${1}===============================
		local result=0
		if [ "X$2" = "Xwebmanager" ];then
			echo backup webmanager config files.
			pushd /home/$iuser/webhome/$2 >/dev/null
				zip -q ../webmanagerConf.zip ./dbconfiglogger.properties ./dbconfig.properties ./webmgr.properties ./WEB-INF/classes/dbconfig.properties ./WEB-INF/classes/config/spring.xml
			popd >/dev/null
			echo backup finish.
		fi
		echo start backup the pub : $2
		find /home/$iuser/webhome/ -maxdepth 1 -name ${2} -type d 2>/dev/null | xargs -n1 -i -t mv -f {} /home/$iuser/backup/bak_$(date +%F)/ || result=2
		if [ $result -eq 0 ]
		then
			echo $1 backup success,now starting update...
			find /tmp/$(date +%m%d)/$dirname/ -name "${1}.*war" -type f | xargs -n1 -i -t unzip -o {} -d /home/$iuser/webhome/$2/ >/dev/null || result=3
			#find /tmp/$(date +%m%d)/$dirname/ -name "${1}.*war" -type f | xargs -n1 -i -t cp {} /home/$iuser/webhome/${2}/
			if [ $result -eq 0 ]
			then
				if [ "X$2" = "Xwebmanager" ];then
					echo update webmanager config files.
					pushd /home/$iuser/webhome/$2 >/dev/null
						unzip -q -o ../webmanagerConf.zip -d .
					popd >/dev/null
					echo update finish.
				fi
				echo $1 update success!
			fi
		else
			echo $1 backup failed!
		fi
		case $result in
			2)
				pubError2=${pubError2}","$2
				;;
			3)
				pubError3=${pubError3}","$2
				;;
			0)
				pubfinish=${pubfinish}","$2
				;;
		esac
		shift 2
	done
}

#确定新版本所在文件夹的名字.
source2=${source%/}
fileName=${source2##/*/}
dirname=${fileName%%.*}
echo new version file name is:$dirname

#创建版本备份与更新目录
if [ ! -z "$dirname" ];then
	if [ ! -d "/tmp/$(date +%m%d)/$dirname" ]
	then
		echo mkdir /tmp/$(date +%m%d)/$dirname
		mkdir -p /tmp/$(date +%m%d)/$dirname
	else
		echo dir:/tmp/$(date +%m%d)/$dirname exist,delete it!
		rm -rf /tmp/$(date +%m%d)/$dirname/*
	fi
else
	echo $source have error! check !
	exit 1
fi
if [ ! -d "/home/$iuser/backup/bak_$(date +%F)" ]
then
	echo mkdir /home/$iuser/backup/bak_$(date +%F)
	mkdir /home/$iuser/backup/bak_$(date +%F)
else
	echo dir:/home/$iuser/backup/bak_$(date +%F) exist,delete it!
	rm -rf /home/$iuser/backup/bak_$(date +%F)/*
fi

#解压新版本并把新版本放到指定目录:(date +%m%d)
if [ -f "$source" ]
then
	file $source | grep "Zip archive data" >/dev/null 2>&1 && {
		echo Extracting $source
		unzip -o $source -d /tmp/$(date +%m%d)/$dirname >/dev/null && echo Extract finish.
	}
fi
if [ -d "$source" ]
then
	echo $source | grep "/tmp/$(date +%m%d)" >/dev/null 2>&1 || {
		echo cp $dirname to /tmp/$(date +%m%d)/$dirname
		cp -r ${source%/}/* /tmp/$(date +%m%d)/$dirname  && echo copy finish.
	}
fi

#开始版本备份与更新
pushd /tmp/$(date +%m%d)/$dirname >/dev/null
	for imod in $(find . -name "*_lib" -type d | awk -F "/" '{print $NF}' | awk -F "_" '{print $1}')
	do
		mod_check $imod
		case $? in
			1)
				modError2=${modError1}","$imod
				;;
			0)
				modCheckOk=${modCheckOk}" "$imod
				;;
		esac
	done
	for ipub in $(find . -name "*.war" -type f | awk -F "/" '{print $NF}' | awk -F "." '{print $1}')
	do
		pubdirname=pub_error
		pub=$ipub;
		case $pub in
			*live*control*)
				pubdirname="livecontrol"
				;;
			*live*interface*)
				pubdirname="liveinterface"
				;;
			*live*room*)
				pubdirname="liveroom"
				;;
			*cmbc*interface*)
				pubdirname="pub_cmbc_interface"
				;;
			*webmanager*)
				pubdirname="webmanager"
				;;
		esac
		pub_check $pubdirname
		case $? in
			1)
				pubError1=${pubError1}","$pub
				;;
			0)
				pubCheckOk=${pubCheckOk}" "$pub" "$pubdirname
				;;
		esac
	done
	echo check result:
	if [ ! -z "$modError1" ];then
		echo mod name error:$modError1
	fi
	if [ ! -z "$pubError1" ];then
		echo pub name error:$pubError1
	fi
	if [ ! -z "$modCheckOk" ];then
		echo mod name ok:$modCheckOk
	fi
	if [ ! -z "$pubCheckOk" ];then
		echo pub name ok:$pubCheckOk
	fi
	printf "Please confirm the result and enter (yes/no) to continue:"
	read x
	if [ "X$x" = "Xyes" ];then
		run "$modCheckOk" "$pubCheckOk"
	else
		printf "Are you want to modify the mod or pub list?(yes/no)"
		read i
		if [ "X$i" = "Xyes" ];then
			printf "Change the module name list (yes/no)\?"
			read y
			if [ "X$y" = "Xyes" ];then
				echo Enter the modname list\(Separated by  s\)\:
				read modCheckOk
				# add check
			fi
			printf "Change the public name list (yes/no)\?"
			read z
			if [ "X$z" = "Xyes" ];then
				echo Enter the pubname list\(Separated by  s\)\:
				read pubCheckOk
				# add check
			fi
			run "$modCheckOk" "$pubCheckOk"
		else
			echo Go to exit\; bye bye\!
			exit 1
		fi
	fi
popd >/dev/null

#最后结果输出
echo ==========================================================
# echo mod total is:${modsum},pub total is:${pubsum}
if [ ! -z "$modError1" ];then
	echo mod name error:$modError1
fi
if [ ! -z "$modError2" ]
then
	echo mod backup failed have:$modError2
fi 
if [ ! -z "$modError3" ];then
	echo mod update failed have:$modError3
fi 
if [ ! -z "$pubError1" ];then
	echo pub name error:$pubError1
fi
if [ ! -z "$pubError2" ]
then
	echo pub backup failed have:$pubError2
fi
if [ ! -z "$pubError2" ];then
	echo pub update failed have:$pubError3
fi
echo mod:${modfinish} finish!
echo pub:${pubfinish} finish!
exit

