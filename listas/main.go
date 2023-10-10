package main
import (
	"fmt"
	"time"
)

func xpto(c chan int, value int) {
	c <- value
}

func main() {
	ch1 := make(chan int)
	ch2 := make(chan int)
	
	for {
		go xpto(ch1, 42)
		go xpto(ch2, 43)

		select {
			case v1 := <-ch1: 
				fmt.Println("valor recebido de ch1:", v1)
			case v2 := <-ch2: 
				fmt.Println("valor recebido de ch1:", v2)
		}

		time.Sleep(time.Second)
	}
}

