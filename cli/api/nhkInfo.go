package api

import (
	"encoding/json"
	"fmt"
	"io"
	"net/http"

	"cli/model"
)

func GetNhkRadio() []model.NhkRadio {

	var nhkRadioList []model.NhkRadio

	// http.Getを用いて外部APIを呼び出す
	resp, err := http.Get("https://www.nhk.or.jp/radioondemand/json/index_v3/index.json")
	// エラーハンドリング
	if err != nil {
		fmt.Println(err)
	} else {
		// io.ReadAllでレスポンスボディを全て読み取る
		data, _ := io.ReadAll(resp.Body)

		var responseObject model.DateLists
		// json.UnmarshalでJSONデータをGoのオブジェクトに変換する
		json.Unmarshal(data, &responseObject)

		m := make(map[string]struct{})

		for _, p := range responseObject.DataList {
			if _, ok := m[p.SiteID]; !ok {
				nhkRadio := model.NhkRadio{
					SiteID:      p.SiteID,
					ProgramName: p.ProgramName,
					DetailJSON:  p.DetailJSON,
				}
				nhkRadioList = append(nhkRadioList, nhkRadio)
			}

		}
	}
	return nhkRadioList
}

// func GetNhkRadioInfo() model.NhkRadio {

// 	var h model.NhkRadio

// 	// http.Getを用いて外部APIを呼び出す
// 	resp, err := http.Get("https://www.nhk.or.jp/radioondemand/json/index_v3/index.json")
// 	// エラーハンドリング
// 	if err != nil {
// 		fmt.Println(err)
// 	} else {
// 		// io.ReadAllでレスポンスボディを全て読み取る
// 		data, _ := io.ReadAll(resp.Body)

// 		var responseObject model.DateLists
// 		// json.UnmarshalでJSONデータをGoのオブジェクトに変換する
// 		json.Unmarshal(data, &responseObject)

// 		m := make(map[string]struct{})

// 		for _, p := range responseObject.DataList {
// 			if _, ok := m[p.SiteID]; !ok {
// 				h.ProgramName
// 				m[p.SiteID] = struct{}{}
// 				tmpList := []string{p.SiteID, p.ProgramName}
// 				newList = append(newList, tmpList)
// 			}

// 		}
// 	}
// 	return newList
