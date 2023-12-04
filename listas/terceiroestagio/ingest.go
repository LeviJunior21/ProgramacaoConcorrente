package main
import (
	"fmt"
)

func request_stream() chan string {
	return make(chan string)
}

func ingest(in chan string) {
	for {
		result := <- in
		fmt.Println(result)
	}
}

func produce(channel chan string, value string) {
	for {
		channel <- value
	}
}

func main() {
	ch1 := request_stream()
	ch2 := request_stream()
	ch3 := request_stream()

	go ingest(ch3)

	go produce(ch1, "a")
	go produce(ch2, "b")
	
	for {
		select {
			case v1 := <- ch1:
				ch3 <- v1
			case v2 := <- ch2:
				ch3 <- v2
		}
	}
}

