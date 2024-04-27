package model

import "time"

type DateLists struct {
	DataList []struct {
		SiteID          string    `json:"site_id"`
		ProgramName     string    `json:"program_name"`
		ProgramNameKana string    `json:"program_name_kana"`
		MediaCode       string    `json:"media_code"`
		CornerID        string    `json:"corner_id"`
		CornerName      string    `json:"corner_name"`
		ThumbnailP      string    `json:"thumbnail_p"`
		ThumbnailC      any       `json:"thumbnail_c"`
		OpenTime        time.Time `json:"open_time"`
		CloseTime       time.Time `json:"close_time"`
		OnairDate       string    `json:"onair_date"`
		LinkURL         any       `json:"link_url"`
		StartTime       time.Time `json:"start_time"`
		UpdateTime      time.Time `json:"update_time"`
		Dev             time.Time `json:"dev"`
		DetailJSON      string    `json:"detail_json"`
	} `json:"data_list"`
}
