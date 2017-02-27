#!/bin/env bash
# writer SY60216

IFS=$' \t\n'

if test $# -lt 2
then
	echo syntax error!
	exit 3
fi

filename=`basename $0`
filedir=$(pwd)
icmd=$1
imod=$2

cpuInfos=`cat /proc/cpuinfo| grep "processor"| wc -l`
meminfos=$(free | awk 'FNR==2{print $2/(1024*1024)}')

if [ `echo $meminfos | awk -v setmem=28 '{print ($1 > setmem)? '1':'0'}'` -eq 1 ]
then
	Xmx="2048m"
	Xms="1024m"
	Xss="512k"
	PermSize="200m"
	MaxPermSize="250m"
	if echo $imod | grep cmp >/dev/null 2>&1
	then
		Xmx="4096m"
		Xms="2048m"
		PermSize="300m"
		MaxPermSize="350m"
	fi
elif [ `echo $meminfos | awk -v setmem=14 '{print ($1 > setmem)? '1':'0'}'` -eq 1 ]
then
	Xmx="1536m"
	Xms="1024m"
	Xss="512k"
	PermSize="100m"
	MaxPermSize="125m"
	if echo $imod | grep cmp >/dev/null 2>&1
	then
		Xmx="1843m"
		Xms="1331m"
		PermSize="200m"
		MaxPermSize="250m"
	fi
else
	echo the memory is too small.
fi

if test "X$icmd" = "Xstart"
then
	pushd $filedir >/dev/null 2>&1
		/home/zhuser/jdk1.7.0_25/bin/java -Xmx$Xmx -Xms$Xms -Xss512k -XX:PermSize=$PermSize -XX:MaxPermSize=$MaxPermSize -XX:+UseG1GC -XX:MaxGCPauseMillis=100 -XX:NewRatio=1 -XX:SurvivorRatio=3 -XX:ConcGCThreads=4 -XX:ParallelGCThreads=$cpuInfos -XX:InitiatingHeapOccupancyPercent=60 -Dio.netty.leakDetectionLevel=advanced -jar $imod.jar >> nohup.out 2>&1 &
	popd >/dev/null 2>&1
elif [ "X$icmd" = "Xstop" ]
then
	ps -ef | grep "/home/zhuser/jdk1.7.0_25/bin/java -Xmx$Xmx -Xms$Xms -Xss512k -XX:PermSize=$PermSize -XX:MaxPermSize=$MaxPermSize -XX:+UseG1GC -XX:MaxGCPauseMillis=100 -XX:NewRatio=1 -XX:SurvivorRatio=3 -XX:ConcGCThreads=4 -XX:ParallelGCThreads=$cpuInfos -XX:InitiatingHeapOccupancyPercent=60 -Dio.netty.leakDetectionLevel=advanced -jar ${imod}.jar" | grep -v grep | awk '{print $2}' | xargs kill $3
else
	echo input error! must be start or stop.
	exit 3
fi




