#!/bin/bash -x

IMG_URL=https://upload.wikimedia.org/wikipedia/commons/thumb/8/87/Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg/2560px-Palace_of_Westminster_from_the_dome_on_Methodist_Central_Hall.jpg
IMG_PATH=/tmp/image.jpg
BASE64_PATH=/tmp/image_base64.txt
JSON_PAYLOAD_PATH=/tmp/json_payload.txt

GOOGLE_API_KEY=$GEMINI_API_KEY

# Download the image
curl -o $IMG_PATH $IMG_URL

if [[ "$(base64 --version 2>&1)" = *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

# Encode the image in base64 and save to a file
base64 $B64FLAGS $IMG_PATH > $BASE64_PATH

# Read the base64-encoded image from the file
BASE64_IMAGE=$(cat $BASE64_PATH)

# Create the JSON payload and save to a file
cat <<EOF > $JSON_PAYLOAD_PATH
{
  "contents": [{
    "parts":[
        {"text": "Caption this image."},
        {
          "inline_data": {
            "mime_type":"image/jpeg",
            "data": "$BASE64_IMAGE"
          }
        }
    ]
  }]
}
EOF

# Send the request using the JSON payload file
curl "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=$GOOGLE_API_KEY" \
    -H 'Content-Type: application/json' \
    -X POST \
    -d @$JSON_PAYLOAD_PATH