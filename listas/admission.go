package main

import (
	"fmt"
	"math/rand"
)

type Request struct {
	valor int
}

const maxCapacity = 10

func exec_req(req Request, id int) {
	fmt.Println("Worker", id, "executando a requisição:", req.valor)
}

func create_req() Request {
	return Request{rand.Intn(10)}
}

func worker(ch chan Request, id int) {
	for {
		valor := <- ch
		exec_req(valor, id)
	}
}

func producer(channel chan Request) {
	for {
		req := create_req()
		channel <- req
	}
}

func main() {
	channel := make(chan Request, maxCapacity)
	barrier := make(chan Request)

	go producer(channel)

	for i := 0; i < maxCapacity; i++ {
		go worker(channel, i)
	}

	<- barrier
}

