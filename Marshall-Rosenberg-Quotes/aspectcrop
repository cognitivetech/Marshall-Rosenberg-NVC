#!/bin/bash
#
# Developed by Fred Weinhaus 10/3/2013 .......... revised 10/12/2014
#
# ------------------------------------------------------------------------------
# 
# Licensing:
# 
# Copyright © Fred Weinhaus
# 
# My scripts are available free of charge for non-commercial use, ONLY.
# 
# For use of my scripts in commercial (for-profit) environments or 
# non-free applications, please contact me (Fred Weinhaus) for 
# licensing arrangements. My email address is fmw at alink dot net.
# 
# If you: 1) redistribute, 2) incorporate any of these scripts into other 
# free applications or 3) reprogram them in another scripting language, 
# then you must contact me for permission, especially if the result might 
# be used in a commercial or for-profit environment.
# 
# My scripts are also subject, in a subordinate manner, to the ImageMagick 
# license, which can be found at: http://www.imagemagick.org/script/license.php
# 
# ------------------------------------------------------------------------------
# 
####
#
# USAGE: aspectcrop [-a aspect] [-g gravity] infile outfile
# USAGE: aspectcrop [-help]
#
# OPTIONS:
#
# -a     aspect      aspect ratio value desired; width to height ratio; values 
#                    can be either a float or as two floats separated by a  
#                    colon; default is input aspect ratio (no change)
# -g     gravity     gravity alignment for cropping; any IM -gravity value; 
#                    default=center
#
###
#
# NAME: ASPECTCROP
# 
# PURPOSE: To crop an image to a specified aspect ratio.
# 
# DESCRIPTION: ASPECTPAD crops an image to a specified aspect ratio.
# 
# OPTIONS: 
# 
# -a aspect ... ASPECT is the desired width to height aspect ratio. Values are 
# either floats>0, such as 2 (landscape) or 0.5 (portrait), or two floats 
# separate by a colon (and no spaces), such a 2:1 (landscale) or 1:2 (portrait).
# The default is input aspect ratio (no change).
# 
# -g gravity ... GRAVITY alignment for cropping; Any IM -gravity setting is 
# allowed. Options are: center (c), north (n), south (s), east (e), west (w), 
# northwest (nw), northeast (ne), southwest, (sw) or southeast (se). The 
# default=center.
# 
# CAVEAT: No guarantee that this script will work on all platforms, 
# nor that trapping of inconsistent parameters is complete and 
# foolproof. Use At Your Own Risk. 
# 
######
#

# set default values
aspect=""
gravity="center"

# set directory for temporary files
dir="."    # suggestions are dir="." or dir="/tmp"

# set up functions to report Usage and Usage with Description
PROGNAME=`type $0 | awk '{print $3}'`  # search for executable on path
PROGDIR=`dirname $PROGNAME`            # extract directory of program
PROGNAME=`basename $PROGNAME`          # base name of program
usage1() 
	{
	echo >&2 ""
	echo >&2 "$PROGNAME:" "$@"
	sed >&2 -e '1,/^####/d;  /^###/g;  /^#/!q;  s/^#//;  s/^ //;  4,$p' "$PROGDIR/$PROGNAME"
	}
usage2() 
	{
	echo >&2 ""
	echo >&2 "$PROGNAME:" "$@"
	sed >&2 -e '1,/^####/d;  /^######/g;  /^#/!q;  s/^#*//;  s/^ //;  4,$p' "$PROGDIR/$PROGNAME"
	}


# function to report error messages
errMsg()
	{
	echo ""
	echo $1
	echo ""
	usage1
	exit 1
	}


# function to test for minus at start of value of second part of option 1 or 2
checkMinus()
	{
	test=`echo "$1" | grep -c '^-.*$'`   # returns 1 if match; 0 otherwise
    [ $test -eq 1 ] && errMsg "$errorMsg"
	}

# test for correct number of arguments and get values
if [ $# -eq 0 ]
	then
	# help information
   echo ""
   usage2
   exit 0
elif [ $# -gt 6 ]
	then
	errMsg "--- TOO MANY ARGUMENTS WERE PROVIDED ---"
else
	while [ $# -gt 0 ]
		do
			# get parameter values
			case "$1" in
		     -help)    # help information
					   echo ""
					   usage2
					   exit 0
					   ;;
				-a)    # get aspect
					   shift  # to get the next parameter
					   # test if parameter starts with minus sign 
					   errorMsg="--- INVALID ASPECT SPECIFICATION ---"
					   checkMinus "$1"
					   aspect=`expr "$1" : '\([.0-9]*[:]*[.0-9]*\)'`
					   [ "$aspect" = "" ] && errMsg "--- ASPECT=$aspect MUST BE ONE OR TWO FLOATS GREATER THAN OR EQUAL TO 0 SEPARATED BY A COLON ---"
					   ;;
				-g)    # get  gravity
					   shift  # to get the next parameter
					   # test if parameter starts with minus sign 
					   errorMsg="--- INVALID GRAVITY SPECIFICATION ---"
					   checkMinus "$1"
					   gravity="$1"
					   gravity=`echo "$gravity" | tr "[:upper:]" "[:lower:]"`
					   case "$gravity" in 
					   		center|c) gravity="center" ;;
					   		north|n) gravity="north" ;;
					   		south|s) gravity="south" ;;
					   		east|e) gravity="east" ;;
					   		west|w) gravity="west" ;;
					   		northwest|nw) gravity="northwest" ;;
					   		northeast|nw) gravity="northeast" ;;
					   		southwest|sw) gravity="southwest" ;;
					   		southeast|se) gravity="southeast" ;;
					   		*) errMsg "--- GRAVITY=$gravity IS AN INVALID VALUE ---" 
					   	esac
					   ;;
				 -)    # STDIN and end of arguments
					   break
					   ;;
				-*)    # any other - argument
					   errMsg "--- UNKNOWN OPTION ---"
					   ;;
		     	 *)    # end of arguments
					   break
					   ;;
			esac
			shift   # next option
	done
	#
	# get infile and outfile
	infile="$1"
	outfile="$2"
fi

# test that infile provided
[ "$infile" = "" ] && errMsg "NO INPUT FILE SPECIFIED"

# test that outfile provided
[ "$outfile" = "" ] && errMsg "NO OUTPUT FILE SPECIFIED"

# setup temporary images
tmpA1="$dir/aspectcrop_1_$$.mpc"
tmpA2="$dir/aspectcrop_1_$$.cache"
trap "rm -f $tmpA1 $tmpA2;" 0
trap "rm -f $tmpA1 $tmpA2; exit 1" 1 2 3 15
trap "rm -f $tmpA1 $tmpA2; exit 1" ERR


# read the input image and test validity.
convert -quiet "$infile" +repage "$tmpA1" ||
	errMsg "--- FILE $infile DOES NOT EXIST OR IS NOT AN ORDINARY FILE, NOT READABLE OR HAS ZERO SIZE  ---"

# get size and aspect ratio of input
ww=`convert $tmpA1 -ping -format "%w" info:`
hh=`convert $tmpA1 -ping -format "%h" info:`
ratio=`convert xc: -format "%[fx:$ww/$hh]" info:`
#echo "ww=$ww; hh=$hh ratio=$ratio;"


# copy input to output if aspect is not specified 
if [ "$aspect" = "" ]; then
	convert $tmpA1 $outfile
	exit
fi

# get aspect
aspect1=`echo $aspect | cut -d\: -f1`
aspect2=`echo $aspect | cut -d\: -f2`
test=`convert xc: -format "%[fx:($aspect2 == $aspect1)?1:0]" info:`
#echo "aspect1=$aspect1; aspect2=$aspect2;"
if [ $aspect1 -eq 0 -o $aspect2 -eq 0 ]; then
	errMsg "--- DESIRED WIDTH OR HEIGHT MUST NOT BE ZERO ---"
elif [ "$aspect2" = "" ]; then
	aspect=$aspect1
elif [ $test -eq 1 ]; then 
	aspect=$aspect1
else
	aspect=`convert xc: -format "%[fx:$aspect1/$aspect2]" info:`
fi
#echo "aspect=$aspect;"



# test if aspect >= ratio
test=`convert xc: -format "%[fx:$aspect>=$ratio?1:0]" info:`
[ $test -eq 1 ] && format="larger" || format="smaller" 
#echo "format=$format;"

# compute width and height of output
if [ "$format" = "larger" ]; then
	width=$ww
	height=`convert xc: -format "%[fx:$hh*$ratio/$aspect]" info:`
elif [ "$format" = "smaller" ]; then
	width=`convert xc: -format "%[fx:$ww*$aspect/$ratio]" info:`
	height=$hh
fi	


# process image
convert $tmpA1 -gravity $gravity -crop ${width}x${height}+0+0 +repage "$outfile"

exit 0

