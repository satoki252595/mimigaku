/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"errors"
	"fmt"

	"cli/api"
	"cli/model"

	"github.com/charmbracelet/huh"
	"github.com/spf13/cobra"
)

// listViewCmd represents the listView command
var listViewCmd = &cobra.Command{
	Use:   "listView",
	Short: "NHKラジオ番組の一覧を出力するコマンド。",
	Long:  `NHKラジオ番組の一覧を出力するコマンド。`,
	Run: func(cmd *cobra.Command, args []string) {
		run()
	},
}

func run() {
	nhkRadioDict := api.GetUrlDict()
	var nhkRadioList []model.NhkRadio

	for k, v := range nhkRadioDict {
		g := model.NhkRadio{
			SiteID:      k,
			ProgramName: v,
		}
		nhkRadioList = append(nhkRadioList, g)

	}

	selectRadio, err := MultipleSelect(nhkRadioList)
	if err != nil {
		fmt.Println(err)
		return
	}
	fmt.Println(selectRadio)

	for k, v := range nhkRadioDict {
		fmt.Printf("> %s %s \n", k, v)
	}

}

func MultipleSelect(nhkRadioList []model.NhkRadio) ([]model.NhkRadio, error) {

	options := make([]huh.Option[model.NhkRadio], 0, len(nhkRadioList))

	for _, v := range nhkRadioList {
		options = append(options, huh.NewOption(v.ProgramName, v))
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
		return errors.New("1個以上選択して下さい（spaceキーで選択できます）")
	}
	return nil
}

func init() {
	rootCmd.AddCommand(listViewCmd)

	// Here you will define your flags and configuration settings.

	// Cobra supports Persistent Flags which will work for this command
	// and all subcommands, e.g.:
	// listViewCmd.PersistentFlags().String("foo", "", "A help for foo")

	// Cobra supports local flags which will only run when this command
	// is called directly, e.g.:
	// listViewCmd.Flags().BoolP("toggle", "t", false, "Help message for toggle")
}
