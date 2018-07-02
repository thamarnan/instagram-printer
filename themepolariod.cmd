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

%convertEXE% "%OUTPUT%.mpc" "%STANDARDRES%.mpc" -geometry +30+120 -composite "%OUTPUT%.mpc"

:: ========== Insert Top Right Corner Timestamp
%convertEXE% "%OUTPUT%.mpc" -fill %DATECOLOR% -undercolor none -pointsize 19 -gravity northeast -annotate +30+30 %CREATEDTIME% "%OUTPUT%.bmp"

:: Removed all images
DEL *.png
DEL *.jpg
DEL *.cache
DEL *.mpc
DEL *.txt
DEL *.cap


rundll32    shimgvw.dll    ImageView_PrintTo /pt   %OUTPUT%.bmp  "Canon IP4500"
