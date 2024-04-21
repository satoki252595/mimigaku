/*
Copyright © 2024 NAME HERE <EMAIL ADDRESS>
*/
package cmd

import (
	"fmt"

	"github.com/spf13/cobra"
)

// listViewCmd represents the listView command
var listViewCmd = &cobra.Command{
	Use:   "listView",
	Short: "NHKラジオ番組の一覧を出力するコマンド。",
	Long:  `NHKラジオ番組の一覧を出力するコマンド。`,
	Run: func(cmd *cobra.Command, args []string) {
		fmt.Println("listView called")
	},
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
