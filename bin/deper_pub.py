#!/usr/bin/envspacepythonPLY#spaceencoding:utf-8PLY__author__space=space'Chocolee'PLYimportspacesysPLYimportspacemultiprocessingPLYimportspacepexpectPLYimportspacetracebackPLYsys.path.append("..")PLYfromspacelib.PublicSQLClassspaceimportspace*PLYfromspacelib.ParamikoClassspaceimportspace*PLYfromspaceoptparsespaceimportspaceOptionParserPLYimportspacerePLYPLYtspace=spaceSQLClass()PLY#全局变量，获取登陆用户属性PLYtomcatlistspace=space['pub_platform','pub_system','webmanager','pub_oauth_interface','pub_cmbc_interface','pub_wcmp','pub_crash_system','pub_es_interface','liveroom','liveinterface','livecontrol']PLYjbosslistspace=space['pub_authorization','pub_groupmsg']PLYhomePathspace=space'/home/zhuser/webhome/'PLYappPathspace=space'/home/zhuser/webapp/'PLYuserspace=space'zhuser'PLYuserInfospace=spacet.findUserPass(user)PLYforspaceispaceinspaceuserInfo:PLYTABportspace=spacei[0]PLYTABpasswdspace=spacestr(i[1])spacePLYPLY#申明帮助信息PLYdefspacehelpFunc(a,b,c,d):PLYTABprintspace"USAGE:"PLYTABprintspace"-hspaceorspace--helpspaceforspacehelp."PLYTABprintspace"-Mspaceorspace--modulespaceforspacemodulename,canspaceusespace','spaceexample:pub_message"PLYTABprintspace"-ispaceorspace--ipspaceforspaceipspaceaddress,canspaceusespace','spaceexample:192.168.199.11,10.10.10.10."PLYTABprintspace"-aspaceorspace--allspaceforspaceallspaceipspaceaddress,listspaceofspacedb."PLYTABprintspace"-Dspaceorspace--deployspaceforspacedeployspaceallspaceapp,usespacethisspaceoptionspacemustspacebespacecareful!"PLYTABprintspace"PUBLIST:pub_interfacespacepub_messagespacepub_message_serverspacepub_platformspacepub_systemspacewebmanager"PLYTABprintspace"EXAMPLE:space'pythonspace%sspace-ispace10.10.10.10space-Mspacepub_platform'"space%sys.argv[0]PLYTABsys.exit(3)PLYPLYdefspacecheck_Ip(ip):PLYTABhostsspace=space[]PLYTABhosts_okspace=space[]PLYTABiphostspace=spacet.findAllHosts()PLYTABforspacehspaceinspaceiphost:PLYTABTABhosts.append(str(h[0]))PLYTABforspaceispaceinspaceip:PLYTABTABifspaceispacenotspaceinspacehosts:PLYTABTABTABprintspace"\033[1;31;40m%sspacemodulespacenotspaceexist,pleasespacecheck!\033[0m"space%iPLYTABTABTAB#continuePLYTABTABTABsys.exit(3)PLYPLYdefspacecheck_ModName(mod):PLYTABmodnamesspace=space[]PLYTABmodulenamespace=spacet.findAllPubName()PLYTABforspacemspaceinspacemodulename:PLYTABTABmodnames.append(str(m[0]))PLYTABforspacemnspaceinspacemod:PLYTABTABifspacemnspacenotspaceinspacemodnames:PLYTABTABTABprintspace"\033[1;31;40mModNamespace%sspacenotspaceexist,pleasespacecheck!\033[0m"space%mnPLYTABTABTABprintspace30*'*'PLYTABTABTABprintspace"\033[1;33;40mInputspaceReferencespaceModName:\033[0m"spacePLYTABTABTABforspacemspaceinspacemodnames:PLYTABTABTABTABprintspace"\033[1;33;40m%s\033[0m"space%m,PLYTABTABTABsys.exit(3)PLYPLY#创建程序目录PLYdefspacemkWebappDir(host):PLYTABpspace=spaceParamikoClass(host,port,user,passwd)PLYTABp.cmd_run('mkdirspace-pspace/opt/webhome')PLYTABp.cmd_run('mkdirspace-pspace/opt/webapp')PLYPLY#执行创建程序目录PLYdefspacemkdirWebapp():PLYTABpoolspace=spacemultiprocessing.Pool(processes=10)PLYTABiplistspace=spacet.findAllHosts()PLYTABforspaceispaceinspaceiplist:PLYTABTABpool.apply_async(mkWebappDir,(i[0],))PLYTABpool.close()PLYTABpool.join()PLYPLY#主进程，通过pexpect远程执行命令PLYdefspacepexRun(host,cmd,password):PLYTABtry:PLYTABTABchildspace=spacepexpect.spawn(cmd)PLYTABTABindexspace=spacechild.expect(['password:','continuespaceconnectingspace(yes/no)?',pexpect.EOF,spacepexpect.TIMEOUT])PLYTABTABifspaceindexspace==space0:PLYTABTABTABchild.sendline(password)PLYTABTABTABchild.interact()PLYTABTABelifspaceindexspace==space1:PLYTABTABTABchild.sendline('yes')PLYTABTABTABchild.expect(['password:'])PLYTABTABTABchild.sendline(password)PLYTABTABTABchild.interact()PLYTABTABelifspaceindexspace==space2:PLYTABTABTABprintspace"space%sspace子程序异常，退出!"space%hostPLYTABTABTABchild.close()PLYTABTABelifspaceindexspace==space3:PLYTABTABTABprintspace"%sspace连接超时"space%hostPLYTABexcept:PLYTABTABtraceback.print_exec()PLYPLYdefspaceis_number(s):PLYTABtry:PLYTABTABfloat(s)PLYTABTABreturnspaceTruePLYTABexceptspaceValueError:PLYTABTABpassPLYPLYTABtry:PLYTABTABimportspaceunicodedataPLYTABTABunicodedata.numeric(s)PLYTABTABreturnspaceTruePLYTABexceptspace(TypeError,spaceValueError):PLYTABTABpassPLYPLYTABreturnspaceFalsePLYPLY#全量部署模块函数PLYdefspacePublicDeploy(info):PLYTABhostspace=spacestr(info[0])PLYTABpubNamespace=spacestr(info[1])PLYTABpubPathspace=spacestr(info[2])PLYTABcpNamespace=spacestr(info[3])PLYTABtailstringspace=spacepubPath.strip().split("_")[-1]PLYTABlocalHomeDirspace=space'%s%s'space%(homePath,pubName)PLYTABlocalTomcatDirspace=space'%stomcat_%s'space%(appPath,pubName)PLYTABremoteHomeDirspace=spacepubPathPLYTABconfDirspace=space'%s'space%remoteHomeDirPLYTABcmdHomespace=space'rsyncspace-arvzspace-espace"sshspace-pspace%s"space%s/space%s@%s:%s'space%(port,localHomeDir,user,host,remoteHomeDir)PLYTABpspace=spaceParamikoClass(host,port,user,passwd)PLYTABifspacepubNamespaceinspacetomcatlist:PLYTABTABifspaceis_number(tailstring):PLYTABTABTABremoteTomcatDirspace=space'/opt/webapp/tomcat_%s_%s'%(pubName,tailstring)PLYTABTABelse:PLYTABTABTABremoteTomcatDirspace=space'/opt/webapp/tomcat_%s'%pubNamePLYTABTABcmdAppspace=space'rsyncspace-arvzspace-espace"sshspace-pspace%s"space%s/space%s@%s:%s'space%(port,localTomcatDir,user,host,remoteTomcatDir)PLYTABTABpexRun(host,cmdApp,passwd)PLYTABTABpexRun(host,cmdHome,passwd)PLYTABTABcmdspace=space'findspace%sspace-namespace"servicesetting.properties"|xargsspacesedspace-ispace"/ComputerName/spaces#CP01#%s#g"'\PLYTABTAB%(confDir,cpName)PLYTABTABp.cmd_run(cmd)PLYTABTABprint('%sspace:uploadspace\033[1;31;40m%s\033[0mspace\033[1;32;40mOK\033[0m'%(host,pubName))PLYTABelse:PLYTABTABpexRun(host,cmdHome,passwd)PLYTABTABcmdspace=space'findspace%sspace-namespace"servicesetting.properties"|xargsspacesedspace-ispace"/ComputerName/spaces#CP01#%s#g"'\PLYTABTAB%(confDir,cpName)PLYTABTABp.cmd_run(cmd)PLYTABTABprint('%sspace:uploadspace\033[1;31;40m%s\033[0mspace\033[1;32;40mOK\033[0m'%(host,pubName))PLYPLY#模块更新函数PLYdefspacePublicDeployUpdate(info):PLYTABhostspace=spacestr(info[0])PLYTABpubNamespace=spacestr(info[1])PLYTABpubPathspace=spacestr(info[2])PLYTABcpNamespace=spacestr(info[3])PLYTABifspacepubNamespaceinspacetomcatlist:PLYTABTABlocalHomeDirspace=space'%s%s'space%(homePath,pubName)PLYTABTABlocalTomcatDirspace=space'%stomcat_%s'space%(appPath,pubName)PLYTABelifspacepubNamespaceinspacejbosslist:PLYTABTABlocalHomeDirspace=space'%s%s_jboss'space%(homePath,pubName)PLYTABTABlocalTomcatDirspace=space'%sjboss_%s'space%(appPath,pubName)PLYTABelse:PLYTABTABlocalHomeDirspace=space'%s%s'space%(homePath,pubName)PLYTABremoteHomeDirspace=spacepubPathPLYTABconfDirspace=space'%s'space%remoteHomeDirPLYTABcmdHomespace=space'rsyncspace-arvzspace--exclude-from="exclude_file.txt"space--deletespace-espace"sshspace-pspace%s"space%s/space%s@%s:%s'space%(port,localHomeDir,user,host,remoteHomeDir)PLYTABpspace=spaceParamikoClass(host,port,user,passwd)PLYTABifspacepubNamespaceinspacetomcatlist:PLYTABTABremoteTomcatDirspace=space'/opt/webapp/'spacePLYTABTABcmdAppspace=space'rsyncspace-arvzspace-espace"sshspace-pspace%s"space%sspace%s@%s:%s'space%(port,localTomcatDir,user,host,remoteTomcatDir)PLYTABTAB#pexRun(host,cmdApp,passwd)PLYTABTABpexRun(host,cmdHome,passwd)PLYTABTABcmdspace=space'findspace%sspace-namespace"servicesetting.properties"|xargsspacesedspace-ispace"/ComputerName/spaces#CP01#%s#g"'\PLYTABTAB%(confDir,cpName)PLYTABTABp.cmd_run(cmd)PLYTABTABprint('%sspace:uploadspace\033[1;31;40m%s\033[0mspace\033[1;32;40mOK\033[0m'%(host,pubName))PLYTABelifspacepubNamespaceinspacejbosslist:PLYTABTABremoteTomcatDirspace=space'/opt/webapp/'PLYTABTABcmdAppspace=space'rsyncspace-arvzspace-espace"sshspace-pspace%s"space%sspace%s@%s:%s'space%(port,localTomcatDir,user,host,remoteTomcatDir)PLYTABTABcmdHomespace=space'rsyncspace-arvzspace--exclude-from="exclude_file.txt"spacespace-espace"sshspace-pspace%s"space%sspace%s@%s:%s'space%(port,localHomeDir,user,host,remoteHomeDir)PLYTABTABpexRun(host,cmdApp,passwd)PLYTABTABpexRun(host,cmdHome,passwd)PLYTABTABprint('%sspace:uploadspace\033[1;31;40m%s\033[0mspace\033[1;32;40mOK\033[0m'%(host,pubName))PLYTABelse:PLYTABTABpexRun(host,cmdHome,passwd)PLYTABTABcmdspace=space'findspace%sspace-namespace"servicesetting.properties"|xargsspacesedspace-ispace"/ComputerName/spaces#CP01#%s#g"'\PLYTABTAB%(confDir,cpName)PLYTABTABp.cmd_run(cmd)PLYTABTABprint('%sspace:uploadspace\033[1;31;40m%s\033[0mspace\033[1;32;40mOK\033[0m'%(host,pubName))PLYPLY#部署计数器PLYdefspacePublicDeployRun():PLYTABlistinfospace=spacet.findALLInfo()PLYTABnspace=space0PLYTABforspaceispaceinspacelistinfo:PLYTABTABPublicDeploy(i)PLYTABTABnspace+=space1PLYTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%nPLYPLY#帮助参数配置PLYparserspace=spaceOptionParser(add_help_option=0)PLYparser.add_option("-h",space"--help",spaceaction="callback",spacecallback=helpFunc)PLYparser.add_option("-M",space"--module",spaceaction="store",spacetype="string",spacedest="module",default="")PLYparser.add_option("-m",space"--mid",spaceaction="store",spacetype="string",spacedest="mid",default="")PLYparser.add_option("-i",space"--ip",spaceaction="store",spacetype="string",spacedest="ip",default="")PLYparser.add_option("-a",space"--all",spaceaction="store_true",spacedest="all")PLYparser.add_option("-D",space"--deploy",spaceaction="store_true",spacedest="deploy")PLYparser.add_option("-n",space"--number",spaceaction="store",spacetype="string",spacedest="number",default="")PLY(options,spaceargs)space=spaceparser.parse_args()PLYipspace=spaceoptions.ip.split(',')PLYmodspace=spaceoptions.module.split(',')PLYmid=options.midPLYallipspace=spaceoptions.allPLYdeployspace=spaceoptions.deployPLYorder=options.number.split(',')PLYcommandoption=argsPLYPLYifspace__name__space==space'__main__':PLYTABifspacelen(sys.argv)space==space1:PLYTABTABhelpFunc('a','b','c','d')PLYTABmodulelistspace=space[]PLYTABiplistspace=space[]PLYTABifspaceipspace!=space['']:PLYTABTABcheck_Ip(ip)PLYTABifspacemodspace!=space['']:PLYTABTABcheck_ModName(mod)PLYTABifspaceorderspace!=space['']:PLYTABTABallipspace=spaceTruePLYTABTABorder_newspace=spaceorderPLYTABTABorderspace=space['']PLYTABTABforspacei,jspaceinspaceenumerate(order_new):PLYTABTABTABjspace=spacere.sub(r'[a-zA-Z]*',"",j,0)PLYTABTABTABifspacej.find("-",0,len(j))space!=space-1:PLYTABTABTABTAB#spacejspace=spacej.upper().replace("CP","")PLYTABTABTABTABoj=j.split('-')PLYTABTABTABTABforspaceiobjspaceinspacerange(int(oj[0]),int(oj[1])+1):PLYTABTABTABTABTABorder.append("CP%s"%iobj)PLYTABTABTABelse:PLYTABTABTABTABorder.append("CP%s"%j)PLYTABTABTABTAB#spaceorder.append(order_new[i].upper())PLYTABifspacemidspace!=space"":PLYTABTABifspacemidspace!=space"head"spaceandspacemidspace!=space"tail":PLYTABTABTABprintspace"\033[1;31;40mmidspacenotspacecorrect,pleasespacecheck!\033[0m"PLYTABTABTABsys.exit(3)PLYTABTABelse:PLYTABTABTABallipspace=spaceTruePLYTABifspacelen(mod)space!=space1spaceandspacemidspace!=space"":PLYTABTABprintspace"\033[1;31;40mmidspaceandspaceseveralspacemodulesspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABTABsys.exit(3)PLYTABifspaceipspace!=space['']spaceandspacemidspace!=space"":PLYTABTABprintspace"\033[1;31;40mmidspaceandspaceipspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABTABsys.exit(3)PLYTABifspacelen(mod)space!=space1spaceandspaceorderspace!=space['']:PLYTABTABprintspace"\033[1;31;40morderspaceandspaceseveralspacemodulesspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABTABsys.exit(3)PLYTABifspaceorderspace!=space['']spaceandspacemidspace!=space"":PLYTABTABprintspace"\033[1;31;40mmidspaceandspaceorderspacenumberspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABTABsys.exit(3)PLYTABifspaceorderspace!=space['']spaceandspaceipspace!=space['']:PLYTABTABprintspace"\033[1;31;40mipspaceandspaceorderspacenumberspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABTABsys.exit(3)PLYPLY#判断模块名和ip地址是否合法PLYTABifspacemodspace!=space['']spaceandspaceipspace!=space['']:PLYTABTABtmplistspace=space[]PLYTABTABinfolistspace=space[]PLYTABTABforspaceispaceinspacemod:PLYTABTABTABforspacenspaceinspaceip:PLYTABTABTABTABtmplist.append(t.findIpModInfo(n,i))PLYTABTABwhilespace[]spaceinspacetmplist:PLYTABTABTABtmplist.remove([])PLYTABTABforspaceispaceinspacetmplist:PLYTABTABTABforspacenspaceinspacei:PLYTABTABTABTABinfolist.append(n)PLYTABTABifspaceinfolistspace!=space[]:PLYTABTABTABmodlenspace=spacespacelen(infolist)PLYTABTABTABcountspace=spacemodlen/2PLYTABTABTABlinfospace=spacemodlen%2PLYTABTABTABifspacelinfospace!=space0:PLYTABTABTABTABcountspace=spacecount+1PLYTABTABTABifspacemidspace==space"head":PLYTABTABTABTABispace=space0PLYTABTABTABTABwhilespaceispace<spacecount:PLYTABTABTABTABTABPublicDeployUpdate(infolist[i])PLYTABTABTABTABTABispace=spacei+1PLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%iPLYTABTABTABelifspacemidspace==space"tail":PLYTABTABTABTABispace=spacecountPLYTABTABTABTABwhilespaceispace<spacemodlen:PLYTABTABTABTABTABPublicDeployUpdate(infolist[i])PLYTABTABTABTABTABispace=spacei+1PLYTABTABTABTABispace=spacemodlen-countPLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%iPLYTABTABTABelse:TABTABPLYTABTABTABTABforspaceispaceinspaceinfolist:PLYTABTABTABTABTABPublicDeployUpdate(i)PLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%modlenPLYTABTABelse:PLYTABTABTABprint('Error!pleasespacecheckspacedbspacefile!!')PLY#按照模块进行部署及更新PLYTABelifspacemodspace!=space['']spaceandspaceallipspace==spaceTrue:PLYTABTABorderStrspace=space""PLYTABTABifspaceorderspace!=space['']:PLYTABTABTABorderStrspace=space"spaceandspace("PLYTABTABTABforspacenspaceinspaceorder:PLYTABTABTABTABorderStrspace=spaceorderStrspace+space"CPname='%s'spaceorspace"%nPLYTABTABTABorderStrspace=spacere.sub(r'spaceorspace$',")",orderStr,0)PLYTABTABtmplistspace=space[]PLYTABTABinfolistspace=space[]PLYTABTABforspaceispaceinspacemod:PLYTABTABTABtmplist.append(t.findIPInfo(i,orderStr))PLYTABTABforspaceispaceinspacetmplist:PLYTABTABTABforspacenspaceinspacei:PLYTABTABTABTABinfolist.append(n)PLYTABTABifspaceinfolistspace!=space[]:PLYTABTABTABmodlenspace=spacespacelen(infolist)PLYTABTABTABcountspace=spacemodlen/2PLYTABTABTABlinfospace=spacemodlen%2PLYTABTABTABifspacelinfospace!=space0:PLYTABTABTABTABcountspace=spacecount+1PLYTABTABTABifspacemidspace==space"head":PLYTABTABTABTABispace=space0PLYTABTABTABTABwhilespaceispace<spacecount:PLYTABTABTABTABTABPublicDeployUpdate(infolist[i])PLYTABTABTABTABTABispace=spacei+1PLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%iPLYTABTABTABelifspacemidspace==space"tail":PLYTABTABTABTABispace=spacecountPLYTABTABTABTABwhilespaceispace<spacemodlen:PLYTABTABTABTABTABPublicDeployUpdate(infolist[i])PLYTABTABTABTABTABispace=spacei+1PLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%(modlen-count)PLYTABTABTABelse:TABTABPLYTABTABTABTABforspaceispaceinspaceinfolist:PLYTABTABTABTABTABPublicDeployUpdate(i)PLYTABTABTABTABprintspace'\033[1;33;40mcount:%s\033[0m'space%modlenPLYTABTABelse:PLYTABTABTABprint('Error!pleasespacecheckspacedbspacefile!!')PLY#全量部署模块PLYTABelifspacedeploy:PLYTABTABinfospace=spaceraw_input('Arespaceyouspacesurespaceusespacethisspaceoption(yes/no):')PLYTABTABifspaceinfospace==space'yes':PLYTABTABTABmkdirWebapp()PLYTABTABTABPublicDeployRun()PLYTABTABelifspaceinfospace==space'no':PLYTABTABTABsys.exit(3)PLYTABTABelse:PLYTABTABTABprintspace'Sorry,mustspacechoicespaceyesspaceorspaceno.'PLYTABelse:PLYTABTABprint('syntaxspaceerror!Pleasespaceusespace-hspaceforspacehelp!')PLY
