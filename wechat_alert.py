CropID='ww37961e59c8b3e598'

Secret='oscujAvuCOEbT_85UUuYoaOtW_-TdtB0CuSzt7b09aU'

GURL="https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=$CropID&corpsecret=$Secret"

Gtoken=$(/usr/bin/curl -s -G $GURL | awk -F\" '{print $4}')

echo $Gtoken

PURL="https://qyapi.weixin.qq.com/cgi-bin/message/send?access_token=$Gtoken"

function body() {

local int AppID=1000004

local UserID=002

local PartyID=2

local Msg=$(echo "$@" | cut -d " " -f3-)

printf '{\n'

printf '\t"touser": "'"$UserID"\"",\n"

printf '\t"toparty": "'"$PartyID"\"",\n"

printf '\t"msgtype": "text",\n'

printf '\t"agentid": "'"$AppID "\"",\n"

printf '\t"text": {\n'

printf '\t\t"content": "'"$Msg"\""\n"

printf '\t"},\n'

printf '\t"safe:":0\n'

printf '}\n'

}

/usr/bin/curl --data-ascii "$(body $1 $2 $3)" $PURL
