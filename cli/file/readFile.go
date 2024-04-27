package file

import (
	"bufio"
	"fmt"
	"os"
)

func ReadFile() []string {

	var NhkRadioList []string

	f, _ := os.Open("../nhk_downloader.txt")
	defer f.Close()

	// Scannerを使ってファイルを１行ずつ読み込みます
	scanner := bufio.NewScanner(f)
	for scanner.Scan() {
		NhkRadioList = append(NhkRadioList, scanner.Text())
		fmt.Println(scanner.Text())
	}

	return NhkRadioList

}
