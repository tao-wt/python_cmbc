#!/usr/bin/envspacepythonPLY#spaceencoding:utf-8PLY__author__space=space'sainter'PLYPLYimportspacesysPLYsys.path.append("..")PLYfromspacelib.LogicSQLClassspaceimportspace*PLYfromspacelib.ParamikoClassspaceimportspace*PLYimportspacesubprocessPLYimportspacemultiprocessingPLYfromspaceoptparsespaceimportspaceOptionParserPLYimportspacerePLYPLYtspace=spaceSQLClass()PLYuseUserspace=space'zhuser'PLYuserInfospace=spacet.findUserPass(useUser)PLYforspaceispaceinspaceuserInfo:PLYTABuserspace=spacei[0]PLYTABportspace=spacei[1]PLYTABpasswdspace=spacei[2]PLYPLYdefspacehelpFunc(a,b,c,d):PLYTABprintspace"USAGE:"PLYTABprintspace"EXAMPLE:space'\033[1;33;40mpythonspace%sspace-ispaceIpAddrspace-MspaceModuleName\033[0m'spaceorspace'\033[1;33;40mpythonspace%sspace-aspace-s\033[0m'"space%(sys.argv[0],sys.argv[0])PLYTABprintspace"-hspaceorspace--helpspaceforspacehelp."PLYTABprintspace"-Mspaceorspace--modulespaceforspacemodulename,canspaceusespace','spaceexample:\033[1;33;40mspacepythonspace%sspace-Mspaceacp,cmp,nav\033[0m"space%sys.argv[0]PLYTABprintspace"-mspaceorspace--midspaceforspacemid,canspaceusespace','spaceexample:\033[1;33;40mspacepythonspace%sspace-mspacehead/tailspace\033[0m"space%sys.argv[0]PLYTABprintspace"-ispaceorspace--ipspaceforspaceipspaceaddress,canspaceusespace','spaceexample:\033[1;33;40mspacepythonspace%sspace-ispace192.168.199.117,192.168.199.118\033[0m"space%sys.argv[0]PLYTABprintspace"-aspaceorspace--allspaceforspaceallspacemodulespacecheck','spaceexample:\033[1;33;40mspacepythonspace%sspace-a\033[0m"space%sys.argv[0]PLYTABsys.exit(3)PLYPLYdefspaceverFunc(a,b,c,d):PLYTABprintspace"Versionspace2.0"PLYTABsys.exit(0)PLYPLYparserspace=spaceOptionParser(add_help_option=0)PLYparser.add_option("-h",space"--help",spaceaction="callback",spacecallback=helpFunc)PLYparser.add_option("-v",space"-V",space"--version",spaceaction="callback",spacecallback=verFunc)PLYparser.add_option("-M",space"--module",spaceaction="store",spacetype="string",spacedest="module",default="")PLYparser.add_option("-m",space"--mid",spaceaction="store",spacetype="string",spacedest="mid",default="")PLYparser.add_option("-n",space"--number",spaceaction="store",spacetype="string",spacedest="number",default="")PLYparser.add_option("-i",space"--ip",spaceaction="store",spacetype="string",spacedest="ip",default="")PLYparser.add_option("-a",space"--all",spaceaction="store_true",spacedest="all",default=False)PLY(options,spaceargs)space=spaceparser.parse_args()PLYmod=options.module.split(',')PLYmid=options.midPLYorder=options.number.split(',')PLYip=options.ip.split(',')PLYall=options.allPLYcommandoption=argsPLYPLYdefspacecheck_Ip(ip):PLYTABhostsspace=space[]PLYTABhosts_okspace=space[]PLYTABiphostspace=spacet.findHosts()PLYTABforspacehspaceinspaceiphost:PLYTABTABhosts.append(str(h[0]))PLYTABipspace=space{}.fromkeys(ip).keys()PLYTABforspaceispaceinspaceip:PLYTABTABifspaceispacenotspaceinspacehosts:PLYTABTABTABprintspace"\033[1;31;40m%sspacenotspaceexist,pleasespacecheck!\033[0m"space%iPLYTABTABTAB#continuePLYTABTABTABsys.exit(3)PLYPLYdefspacecheck_ModName(mod):PLYTABmodnamesspace=space[]PLYTABmodulenamespace=spacet.findModName()PLYTABforspacemspaceinspacemodulename:PLYTABTABmodnames.append(str(m[0]))PLYTABforspacemnspaceinspacemod:PLYTABTABifspacemnspacenotspaceinspacemodnames:PLYTABTABTABprintspace"\033[1;31;40mModNamespace%sspacenotspaceexist,pleasespacecheck!\033[0m"space%mnPLYTABTABTABprintspace30*'*'PLYTABTABTABprintspace"\033[1;33;40mInputspaceReferencespaceModName:\033[0m"spacePLYTABTABTABforspacemspaceinspacemodnames:PLYTABTABTABTABprintspace"\033[1;33;40m%s\033[0m"space%m,PLYTABTABTABsys.exit(3)PLYPLYdefspacecheckmoduleinfo(moduleinfo):PLYTABhostspace=spacemoduleinfo[0]PLYTABmoduleportspace=spacemoduleinfo[1]PLYTABpathspace=spacemoduleinfo[2]PLYTABmodulerunnamespace=spacepath.split('/')[-1]PLYTABpspace=spaceParamikoClass(host,port,user,passwd)PLYTABpsspace=space"psspace-ef|grepspace%s.jar|grepspace-vspacesupervise|grepspace-vspacegrepspace>space/dev/nullspace&&spaceechospace'1'space||spaceechospace'0'"space%(modulerunname)PLYTABresult_psspace=spacep.check_cmd(ps).strip()PLYTAB##addspacenetstatPLYTABportnumberspace=spacelen(moduleport.split(";"))PLYTABifspaceportnumberspace==space2:PLYTABTABcountspace=space0PLYTABTABforspaceispaceinspacemoduleport.split(";"):PLYTABTABTABcmd_netstatspace=space"netstatspace-an|grepspaceLISTEN|grepspacetcp|grepspace-wspace'%s'|wcspace-l"space%(i)PLYTABTABTABresult_netstat_countspace=spaceint(p.check_cmd(cmd_netstat).strip())PLYTABTABTABcountspace=spacecountspace+spaceresult_netstat_countPLYTABTABifspacecountspace==spaceportnumberspaceandspaceresult_psspace==space'1':PLYTABTABTABprintspace"%sspace%sspace%sspace\033[1;32;40mstartspaceOK\033[0m"space%(host,modulerunname,moduleinfo[3])PLYTABTABelse:PLYTABTABTABprintspace"%sspace%sspace%sspace\033[1;31;40mnotspacestart\033[0m"space%(host,modulerunname,moduleinfo[3])PLYTABelifspaceportnumberspace==space1:PLYTABTABcmd_netstatspace=space"netstatspace-an|grepspaceLISTEN|grepspacetcp|grepspace-wspace'%s'space>space/dev/nullspace&&spaceechospace'1'space||spaceechospace'0'"space%(moduleport)PLYTABTABresult_netstatspace=spacep.check_cmd(cmd_netstat).strip()PLYTABTABifspaceresult_netstatspace==space'1'spaceandspaceresult_psspace==space'1':PLYTABTABTABprintspace"%sspace%sspace%sspace\033[1;32;40mstartspaceOK\033[0m"space%(host,modulerunname,moduleinfo[3])PLYTABTABelse:PLYTABTABTABprintspace"%sspace%sspace%sspace\033[1;31;40mnotspacestart\033[0m"space%(host,modulerunname,moduleinfo[3])PLYPLYdefspacemultipoolcess(moduleinfo):PLYTABpoolspace=spacemultiprocessing.Pool(processes=8)PLYTAB#spacemodlenspace=spacespacelen(moduleinfo)PLYTAB#spacecountspace=spacemodlen/2PLYTAB#spacelinfospace=spacemodlen%2PLYTAB#spaceifspacelinfospace!=space0:PLYTABTAB#spacecountspace=spacecount+1PLYTAB#spaceifspacemidspace==space"head":PLYTABTAB#spaceispace=space0PLYTABTAB#spacewhilespaceispace<spacecount:PLYTABTABTAB#spacepool.apply_async(checkmoduleinfo,(moduleinfo[i],))PLYTABTABTAB#spaceispace=spacei+1PLYTAB#spaceelifspacemidspace==space"tail":PLYTABTAB#spaceispace=spacecountPLYTABTAB#spacewhilespaceispace<spacemodlen:PLYTABTABTAB#spacepool.apply_async(checkmoduleinfo,(moduleinfo[i],))PLYTABTABTAB#spaceispace=spacei+1PLYTAB#spaceelse:PLYTABforspaceispaceinspacemoduleinfo:PLYTABTABpool.apply_async(checkmoduleinfo,(i,))PLYTABpool.close()PLYTABpool.join()PLYPLY#检查参数:ip,mod,mid是否合法兼容PLYifspaceipspace!=space['']:PLYTABcheck_Ip(ip)PLYifspacemodspace!=space['']:PLYTABcheck_ModName(mod)PLYPLYifspacemidspace!=space"":PLYTABifspacemidspace!=space"head"spaceandspacemidspace!=space"tail":PLYTABTABprintspace"\033[1;31;40mmidspacenotspacecorrect,pleasespacecheck!\033[0m"PLYTABTABsys.exit(3)PLYifspaceorderspace!=space['']:PLYTABorder_newspace=spaceorderPLYTABorderspace=space['']PLYTABforspacei,jspaceinspaceenumerate(order_new):PLYTABTABjspace=spacere.sub(r'[a-zA-Z]*',"",j,0)PLYTABTABifspacej.find("-",0,len(j))space!=space-1:PLYTABTABTAB#spacejspace=spacej.upper().replace("CP","")PLYTABTABTABoj=j.split('-')PLYTABTABTABforspaceiobjspaceinspacerange(int(oj[0]),int(oj[1])+1):PLYTABTABTABTABorder.append("CP%s"%iobj)PLYTABTABelse:PLYTABTABTABorder.append("CP%s"%j)PLYTABTABTAB#spaceorder.append(order_new[i].upper())PLYTABTAB#whilespace[]spaceinspaceorder:PLYTABTABTAB#order.remove([])PLYPLY#spaceifspacelen(mod)space!=space1spaceandspacemidspace!=space"":PLYTAB#spaceprintspace"\033[1;31;40mmidspaceandspaceseveralspacemodulesspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTAB#spacesys.exit(3)PLYifspacelen(mod)space!=space1spaceandspaceorderspace!=space['']:PLYTABprintspace"\033[1;31;40morderspaceandspaceseveralspacemodulesspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABsys.exit(3)PLYifspaceipspace!=space['']spaceandspacemidspace!=space"":PLYTABprintspace"\033[1;31;40mmidspaceandspaceipspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABsys.exit(3)PLYifspaceorderspace!=space['']spaceandspacemidspace!=space"":PLYTABprintspace"\033[1;31;40mmidspaceandspaceorderspacenumberspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABsys.exit(3)PLYifspaceorderspace!=space['']spaceandspaceipspace!=space['']:PLYTABprintspace"\033[1;31;40mipspaceandspaceorderspacenumberspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABsys.exit(3)PLYifspaceorderspace!=space['']spaceandspaceallspace==spaceTrue:PLYTABprintspace"\033[1;31;40m-aspaceandspaceorderspacenumberspacecannotspaceusespacetogether,pleasespacemodify!\033[0m"PLYTABsys.exit(3)PLYPLYtmplistspace=space[]PLYmoduleinfospace=space[]PLYiplistspace=space[]PLYdefspacemoduleappend(list):PLYTABnewListspace=space[]PLYTABforspaceispaceinspacelist:PLYTABTABforspacenspaceinspacei:PLYTABTABTABnewList.append(n)PLYTABreturnspacenewListPLYPLY#ip_checkPLYifspaceipspace!=space['']spaceandspacemodspace==space['']:PLYTABforspaceispaceinspaceip:PLYTABTABtmplist.append(t.findModByIP(i))PLYTABmoduleinfospace=spacemoduleappend(tmplist)PLYTABmultipoolcess(moduleinfo)PLY#mod_checkPLYelifspacemodspace!=space['']spaceandspaceipspace==space['']:PLYTABorderStrspace=space""PLYTABifspaceorderspace!=space['']:PLYTABTAB#printspaceorderPLYTABTABifspace''spaceinspaceorder:PLYTABTABTABorder.remove('')PLYTABTAB#printspaceorderPLYTABTABorderStrspace=space"spaceandspace("PLYTABTABforspacenspaceinspaceorder:PLYTABTABTABorderStrspace=spaceorderStrspace+space"CPname='%s'spaceorspace"%nPLYTABTABorderStrspace=spacere.sub(r'spaceorspace$',"",orderStr,0)space+space")"PLYTAB#printspaceorderStrPLYTABforspacemspaceinspacemod:PLYTABTABgetListspace=space[]PLYTABTABgetList.append(t.findModByModName(m,orderStr))PLYTABTABlistspace=spacemoduleappend(getList)PLYTABTABmodlenspace=spacespacelen(list)PLYTABTABcountspace=spacemodlen/2PLYTABTABlinfospace=spacemodlen%2PLYTABTABifspacelinfospace!=space0:PLYTABTABTABcountspace=spacecount+1PLYTABTABifspacemidspace==space"head":PLYTABTABTABispace=space0PLYTABTABTABwhilespaceispace<spacecount:PLYTABTABTABTABmoduleinfo.append(list[i])PLYTABTABTABTABispace=spacei+1PLYTABTABelifspacemidspace==space"tail":PLYTABTABTABispace=spacecountPLYTABTABTABwhilespaceispace<spacemodlen:PLYTABTABTABTABmoduleinfo.append(list[i])PLYTABTABTABTABispace=spacei+1PLYTABTABelse:PLYTABTABTABforspaceispaceinspacelist:PLYTABTABTABTABmoduleinfo.append(i)PLYTAB#spaceforspacemspaceinspacemod:TABPLYTABTAB#spacetmplist.append(t.findModByModName(m,orderStr))PLYTAB#spacemoduleinfospace=spacemoduleappend(tmplist)PLYTABmultipoolcess(moduleinfo)PLY##mod_and_ip_checkPLYelifspacemodspace!=space['']spaceandspaceipspace!=space['']:PLYTABforspaceispaceinspaceip:PLYTABTABforspacemspaceinspacemod:PLYTABTABTABtmplist.append(t.findModByModAndIP(i,m))PLYTABmoduleinfospace=spacemoduleappend(tmplist)PLYTABmultipoolcess(moduleinfo)PLY##check_allPLYelifspaceallspace==spaceTrue:PLYTABipspace=spacet.findHosts()PLYTABforspaceispaceinspaceip:PLYTABTABiplist.append(str(i[0]))PLYTABforspaceispaceinspaceiplist:PLYTABTABtmplist.append(t.findModByIP(i))PLYTABmoduleinfospace=spacemoduleappend(tmplist)PLYTABmultipoolcess(moduleinfo)PLYelse:PLYTABprint('\033[1;31;40mInputspaceError!!!pleasespaceusespace-hspaceforspacehelp!!!\033[0m')PLY
