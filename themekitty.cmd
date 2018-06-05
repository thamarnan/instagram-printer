@ECHO OFF
SET CAPTION=%7
SET LIKESCOUNT=%6
SET CREATEDTIME=%5
SET	STANDARDRES=%4
SET PROFILEPICT=%3
SET LOCATION=%2
SET USERNAME=%1

SET TIMESTAMP=%TIME:~0,2%_%TIME:~3,2%_%TIME:~6,2%
SET CONVMK="%~n0\template_conversation.png"
SET BACKGROUND="%~n0\template_whitebackground.bmp"
SET LOCATIONMK="%~n0\template_location.png"
SET LIKEMK="%~n0\template_heart.png"
REM SET OUTPUT=%~n0-%TIMESTAMP%
SET OUTPUT=FINAL-%TIMESTAMP%

SET USERNAMECOLOR="#105b94"
SET LOCATIONCOLOR="#4c93d1"
SET DATECOLOR="#a0a1a5"

SET convertEXE="imagemagick\convert.exe"

%convertEXE% "%STANDARDRES%" -shave 1x1 -bordercolor black -border 1 "%STANDARDRES%.mpc"

%convertEXE% -size 150x150 xc:none -fill "%PROFILEPICT%" -draw "circle 74,74 74,1" PNG32:"%PROFILEPICT%.png"

%convertEXE% "%PROFILEPICT%.png" -resize 75x75 "%PROFILEPICT%.png"

%convertEXE% %BACKGROUND% %PROFILEPICT%.png -geometry +30+30 -composite "%OUTPUT%.mpc"
%convertEXE% "%OUTPUT%.mpc" "%STANDARDRES%.mpc" -geometry +30+120 -composite "%OUTPUT%.mpc"

if %LOCATION% == "null" (
	%convertEXE% "%OUTPUT%.mpc" -fill "%USERNAMECOLOR%" -undercolor none -pointsize 24 -annotate +120+72 %USERNAME% "%OUTPUT%.mpc"
) else (

	%convertEXE% "%OUTPUT%.mpc" %LOCATIONMK% -geometry +116+72 -composite "%OUTPUT%.mpc"
	%convertEXE% "%OUTPUT%.mpc" -fill "%USERNAMECOLOR%" -undercolor none -pointsize 24 -annotate +120+56 "%USERNAME%" "%OUTPUT%.mpc"
	%convertEXE% "%OUTPUT%.mpc" -fill "%LOCATIONCOLOR%" -undercolor none -pointsize 22 -annotate +136+90 %LOCATION% "%OUTPUT%.mpc"
)

:: ========== Check LIKE is more than zero then print Like
	if %LIkESCOUNT% GTR "0" (
		%convertEXE% "%OUTPUT%.mpc" %LIKEMK% -geometry +30+775 -composite "%OUTPUT%.mpc"
		%convertEXE% "%OUTPUT%.mpc" -fill "%USERNAMECOLOR%" -undercolor none -pointsize 22 -annotate +60+793 "%LIKESCOUNT% likes" "%OUTPUT%.mpc"
)

findstr /m "null" %CAPTION% > tmp.txt
if not %errorlevel% == 0 (
	:: ========== Insert Conversation Icon
	%convertEXE% "%OUTPUT%.mpc" %CONVMK% -geometry +30+806 -composite "%OUTPUT%.mpc"
	:: ========== Generate Conversation Text
	%convertEXE% -size 600x -font %systemroot%\fonts\tahoma.ttf -pointsize 22 -background none -fill %USERNAMECOLOR% caption:@%CAPTION% PNG32:"CONV_%PROFILEPICT%".png
	%convertEXE% "%OUTPUT%.mpc" "CONV_%PROFILEPICT%".png -geometry +60+800 -composite "%OUTPUT%.mpc"
)

:: ========== Insert Top Right Corner Timestamp
%convertEXE% "%OUTPUT%.mpc" -fill %DATECOLOR% -undercolor none -pointsize 19 -gravity northeast -annotate +30+30 %CREATEDTIME% "%OUTPUT%.bmp"

DEL *.png
DEL *.jpg
DEL *.cache
DEL *.mpc
DEL *.txt
DEL *.cap

rundll32    shimgvw.dll    ImageView_PrintTo /pt   %OUTPUT%.bmp  "Canon IP4500"
