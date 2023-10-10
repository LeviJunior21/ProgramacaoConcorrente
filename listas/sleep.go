package main

import (
	"fmt"
	"os"
	"time"
	"math/rand"
	"strconv"
)

func sleep(ch chan int, id int) {
	tempoAleatorio := rand.Intn(6)
	duracao := time.Duration(tempoAleatorio) * time.Second
	fmt.Println("Thread", id, ": Dormindo por", tempoAleatorio, "segundos")
	time.Sleep(duracao)
	fmt.Println("Thread", id, ": Acordei depois de", tempoAleatorio, "segundos")
	ch <- 1
}

func main() {
	num_process, err := strconv.Atoi(os.Args[1])
	if err != nil {fmt.Println(err)}
	
	ch := make(chan int, num_process)
	
	for i := 0; i < num_process; i++ {
		go sleep(ch, i)
	}
	
	for i := 0; i < num_process; i++ {
		<- ch
	}

	fmt.Println(num_process)
}
