package file

import (
	"cli/model"
	"fmt"
	"os"
	"strings"
)

func WriteFile(selectNhkRadioList []model.NhkRadio) {
	f, _ := os.Create("../nhk_downloader.txt")
	defer f.Close()

	for _, nhk := range selectNhkRadioList {

		url := nhk.DetailJSON
		pattern := "_01.json"

		// strings パッケージの HasSuffix 関数を使うと、文字列の末尾が特定の文字列であるかどうかを判定することができます。
		check := strings.HasSuffix(url, pattern)

		if check {

			data := []byte(nhk.DetailJSON + "\n")

			_, err := f.Write(data) // buf to writer
			if err != nil {
				fmt.Println(err)
				return
			}

		}

	}

}
