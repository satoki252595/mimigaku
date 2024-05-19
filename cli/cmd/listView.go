/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"errors"
	"fmt"

	"cli/api"
	"cli/file"
	"cli/model"

	"github.com/charmbracelet/huh"
	"github.com/spf13/cobra"
	"golang.org/x/exp/slices"
)

// listViewCmd represents the listView command
var listViewCmd = &cobra.Command{
	Use:   "listView",
	Short: "NHKラジオ番組の一覧を出力するコマンド。",
	Long:  `NHKラジオ番組の一覧を出力するコマンド。選択済みの番組はデフォルトで選択済みとなっています。`,
	Run: func(cmd *cobra.Command, args []string) {
		run()
	},
}

func run() {
	nhkRadioList := api.GetNhkRadio()
	selectedRadioList, err := MultipleSelect(nhkRadioList)
	if err != nil {
		fmt.Println(err)
		return
	}
	file.WriteFile(selectedRadioList)

}

func containsFunctionWithSlicesPkg(slice []string, key string) bool {
	return slices.Contains(slice, key)
}

func MultipleSelect(nhkRadioList []model.NhkRadio) ([]model.NhkRadio, error) {

	options := make([]huh.Option[model.NhkRadio], 0, len(nhkRadioList))
	downloadFileList := file.ReadFile()

	for _, v := range nhkRadioList {
		//options = append(options, huh.NewOption(v.ProgramName, v))
		if containsFunctionWithSlicesPkg(downloadFileList, v.DetailJSON) {
			options = append(options, huh.NewOption(v.ProgramName, v).Selected(true))
		} else {
			options = append(options, huh.NewOption(v.ProgramName, v))
		}

	}

	selectedRadioList := []model.NhkRadio{}

	form := huh.NewForm(
		huh.NewGroup(
			huh.NewMultiSelect[model.NhkRadio]().
				Options(options...).
				Title("ラジオ番組一覧").
				Value(&selectedRadioList).
				Validate(validateMultiSelect),
		),
	)

	err := form.Run()
	if err != nil {
		return []model.NhkRadio{}, err
	}

	return selectedRadioList, nil

}

func validateMultiSelect(selectedNewsList []model.NhkRadio) error {
	if len(selectedNewsList) == 0 {
		return errors.New("1個以上選択して下さい")
	}
	return nil
}

func init() {
	rootCmd.AddCommand(listViewCmd)
}
