#!/bin/bash

# PGP message encryption and decryption in ASCII

# Functions

encrypt()
{
        echo "encrypting $message with $recipient public key"

        # create file with message
        echo $message > temp.txt

        # encrypt message
        gpg -e -a -r "$recipient" --always-trust ./temp.txt

        # print encrypted message
        cat temp.txt.asc

        # delete file
        rm temp.txt

        # delete file
        rm temp.txt.asc
} # end of encrypt function

encrypt-sign()
{
        echo "encrypting $message with $recipient public key"

        # create file with message
        echo $message > temp.txt

        # encrypt message
        gpg -es -a -r "$recipient" --always-trust ./temp.txt

        # print encrypted message
        cat temp.txt.asc

        # delete file
        rm temp.txt

        # delete file
        rm temp.txt.asc
} # end of encrypt-sign function

decrypt()
{
        echo decrypt

        # create file with message
        nano temp.asc

        # decrypt message
        gpg -d temp.asc

        # delete file
        rm temp.asc
} # end of decrypt function

import()
{
        echo import

        # create file for the public key
        nano temp.txt

        # import key
        gpg --import temp.txt

        # delete file
        rm temp.txt
} # end of import function

help()
{
        echo "Spencer Kotys gpg messenger 2020"
        echo "Help Page"
        echo "This is a bash program created by Spencer Kotys, it eliminates the need to create files when encrypting, decrypting, or importing gpg keys and messages"
        echo "Syntax:"
        echo " ./program [-option] [message] [recipient] for options e and es"
        echo " ./program [-option] for options d, i, and h"
        echo "Options: -e: encrypt, -es: encrypt and sign, -d: decrypt, -i: import key, -h: help"
        exit
} # end of help function

# Main

message=
recipient=

while [[ $1 != "" ]] ;
do
        case $1 in
                "-e" )
                        shift
                        message="$1"
                        shift
                        recipient="$1"
                        encrypt ;;
                "-es")
                        shift
                        message="$1"
                        shift
                        recipient="$1"
                        encrypt-sign ;;
                "-d" )
                        decrypt ;;
                "-i" )
                        import ;;
                "-h" )  
                        help ;;
        esac
        shift
done
