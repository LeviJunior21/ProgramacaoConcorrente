# Levi de Lima Pereira Júnior

## Programação Concorrente - UFCG

### 1 - Considere os algoritmos LockOne e LockTwo. Indique exemplos de execução, para cada um dos algoritmos, em que são quebrados requisitos de segurança e/ou progresso. Explique quais os problemas que acontecem em cada caso. Use a seguinte notação para indicar os exemplos de execução (T0_5 -> T0_6 -> T1_5). Essa notação indica que a thread T0 executou as linhas 5 e 6 e depois a thread T1 executou a linha 5.

    1public class LockOne {
    2    private Boolean[] flags;
    3
    4	    public LockOne() {
    5		      this.flags = {False, False}
    6	    }
    7
    8	    public void lock() {
    9		      int myID = Thread.getID();
    10		    this.flags[myID] = True;
    11	      while (this.flags[1 - myID]);
    12    }
    13}

T0_10 -> T1_10 -> T0_11
Depois disso, as threads entram em Deadlock pois ambas estão querendo entrar na região crítica.

    1public class LockTwo {
    2    private int victim;
    3
    4    public void lock() {
    5		     int myID = Thread.getID();
    6		     this.victim = myID;
    7		     while (this.victim == myID);
    8    }
    9}

T0_6 -> T0_7
Fica em loop quando executa completamente até chegar outra thread que escreva que ela é a vítima e assim, a Thread 0 entra na região crítica.
Não tem progresso enquanto não tiver outra Thread que libere.


### 2 - Explique como o algoritmo de Peterson garante que os problemas apresentados nos algoritmos LockOne e LockTwo são resolvidos.
    
    1public class Peterson {
    2    private Boolean[] flags;
    3	   private int victim;
    4
    5	   public Peterson() {
    6		     this.flags = {False, False};
    7	   }
    8
    9	   public void lock() {
    10	     int myID = Tread.gerID();
    11		   this.flags[myID] = True;
    12		   this.victim = myID;
    13		   while (this.flags[1 - myID] && this.victim == myID);
    14   }
    15	
    16	 public void unlock() {
    17	     int myID = Thread.getID();
    18	     this.flags[myID] = False;
    19	 }
    20}

Começamos provando que não tem starvation.
Por contradição, suponha que tem starvation.
Como só temos duas Threads, Thread A e Thread B, podemos supor sem perda de generalidade que a Thread A está executando eternamente o método lock.
Se ela está travada no método Lock é porque está travada no while esperando até que a flag de B se torne falsa ou a vítima é setada para B.

O que B pode está fazendo enquanto a Thread A não tem progresso, talvez B esteja entrando e saindo repetidamente, se for isso então B seta vítima para B assim que reentrar na sessão crítica, uma vez que vítima é B, isso não muda. Logo, a Thread A deve passar do método lock. Isso contradiz a hipótese de que Thread A deve estar eternamente no método Lock.

Se a Thread B não está entrando e saindo repetidamente na região crítica é porque Thread B também está travado no método Lock esperando que ou a Flag A se torne falsa ou A seja a vítima. A Thread A está travada no Lock, então a vítima tem que ser A, mas B também está travado no Lock então a vítima também tem que ser B mas a vítima não pode ser tanto A quanto B, pois a variável vítima só pode assumir um valor.

Essa contradição final prova que Peterson não tem Starvation. Logo, não tem Deadlock.




### 3 - Explique como travas TTAS podem ter desempenho melhor que travas TAS. Sua explicação deve considerar aspectos de arquitetura de computadores.
    
    public class TTAS {
        private AtomicBoolean b;
    
        public TTAS() {
    		    this.b = new AtomicBoolean(False);
        }
    
    	  public void lock() {
    		    while (True) {
    			      while(b.get());
    			      if (!b.getAndSet(True)) {
    				        break;
                }
            }
        }
    
        public void unlock() {
    	      b.set(False);
        }
    }
>
>
    
    public class TAS {
        private AtomicBoolean b;
    
    	  public TAS() {
    		    this.b = new AtomicBoolean(False);
        }
    
    	  public void lock() {
    		    while(b.getAndSet(True));
        }
    
        public void unlock() {
    	      b.set(False);
        }
    }

Todo processador tem uma memória cache, que é uma memória de alta velocidade.
Um acesso à memória exige muito mais ciclos de processamento do que acesso ao cache.
No TAS, cada chamada ao getAndSet() é anunciado no barramento, como todas as Threads querem usar o barramento para se comunicar com a memória, essas chamadas de getAndSet() atrasam todas as Thread, até mesmo aquela Threads que não estão esperando pelo Lock.
Essa chamada forçam outros processadores a descartar suas cópias de cache e todas as Threads que estão rodando ao fazer getAndSet() vai dar “cache miss” quase toda vez e, portanto, devem usar o barramento para pegar o novo valor.

Com TTAS, enquanto o Lock é tido pela Thread A, a Thread B vai dá cache miss na primeira vez que tentar ler o Lock, forçando B a bloquear enquanto o outro valor é carregado na cache de B. Desde que A continue tendo Lock, então B só vai ler o valor, mas vai dar cache hit toda vez e portanto não vai produzir tráfego no barramento.



### 4 - Considere a implementação BrokenBakery. Que problemas, de progresso e segurança, essa implementação incorreta do algoritmo apresenta.
  
    class BrokenBakery implements Lock {
        private volatile int[] ticket;
    
        public Bakery (int n) {
            ticket = new int[n];
            for (int i = 0; i < n; i++) {
                ticket[i] = 0;
            }
        }
    
        public void lock() {
            int id = Thread.getID()
            for (int j = 0; j < n; j++) {
                if (ticket[j] > ticket[id]) {
                    ticket[id] = ticket[j];
                }
    		    }
            
            ticket[id]++;
    
            for (int j = 0; j < n; j++) {
                while ((ticket[j] != 0) && ((ticket[j] < ticket[id]));
            }
        }
    
        public void unlock() {
            int id = Thread.getID()
            ticket[id] = 0;
        }
    }
    

>
>
 
    class BrokenBakery implements Lock {
        private volatile int[] ticket;
        private volatile boolean[] choosing;
    
        public Bakery (int n) {
            ticket = new int[n];
            for (int i = 0; i < n; i++) {
                ticket[i] = 0;
            }
        }
    	
        public void lock() {
            int id = Thread.getID()
            this.choosing[id] = True;
        
            for (int j = 0; j < n; j++) {
                if (ticket[j] > ticket[id]) {
                    ticket[id] = ticket[j];
                }
    		    }
      
            ticket[id]++;
            this.choosing[id] = False;
    
            for (int j = 0; j < n; j++) {
    	          while(this.choosing[j]);
                while (((ticket[j] != 0) && (ticket[j] < ticket[id])) || ((this.tickets[j] == this.tickets[id]) && j < id));
            }
        }
    
        public void unlock() {
            int id = Thread.getID()
            ticket[id] = 0;
        }
    }

1 - while ((ticket[j] != 0) && ((ticket[j] < ticket[id]));
Nesse trecho temos um problema onde se duas Threads tem valores de tickets iguais, ambas entram na região crítica.
Então, para desempatar, devemos desempatar pelo id das Thread quando ambas escolherem o mesmo ticket implementando essa parte adicional na condição || (this.tickets[j] == this.tickets[id]) && j < id) para implementar a prioridade.

2 - Se thread 0 executa e escolhe um valor do ticket igual a 1 e antes de atribuir ela perder a CPU. A Thread 1 ganha a CPU e calcula o seu ticket igual a 1 por exemplo, só que ela consegue atribuir e passar pelo while e entrar na região crítica. 
A Thread 0 ganha a CPU e atribui o ticket, só que quando entra no while.
Ela vê que outra Thread tem maior prioridade e por desempate vai ver que não e ela também entra na região crítica. Por isso usamos o array de booleans e while para ele no for.

### 5 - Refatore a implementação do algoritmo Bakery usando AtomicInt e AtomicBoolean. Simplifique o código ao máximo.

    public class Bakery {
        private AtomicInteger ticketCounter;
    	  private int[] tickets;
        private int n;
    
    	  public Bakery(int n) {
            this.ticketCounter = new AtomicInteger(0);
    		    this.tickets = new int[n];
    		    this.n = n;
        }
    
        public void lock() {
    	      int myID = Thread.getID();
    	      this.tickets[myID] = this.ticketCounter.incrementAndGet();
    
    	      for (int i = 0; i < this.n; i++) {
    		        while (this.tickets[i] != 0 &&this.tickets[i] < this.tickets[myID]);
            }
        }
    
        public void unlock() {
            int myId = Thread.getID()
            ticket[id] = 0;
        }
    }

Quando é melhor usar cada um dos algoritmos que garantem exclusão mútua?

É melhor usar Semáforo quando o tempo de execução do processo é grande, pois os processos grandes serão bloqueados e ajuda pois não gastamos ciclos de CPU num processo que não consegue entrar na região crítica por um longo período de tempo.
Caso usássemos spinlock invés de Semáforo para processos grandes, iremos usar vários ciclos de CPU para um processo que não pode executar por um longo período de tempo, por isso é melhor bloqueá-lo.

Spinlocks são usados quando o tempo de execução da região crítica é pequeno e assim, ela sempre estará nos processos prontos para rodar durante um período curto de tempo.
São exemplos de SpinLocks:

TAS é uma instrução de máquina para um número ilimitado de Threads. Ele retorna o valor booleano anterior a chamada do TAS e tenta colocar True caso o valor atual seja False.
Deve-se usar quando a concorrência é moderada, sem número alto de Threads.

TTAS é uma otimização do TAS onde tentamos ver se a bandeira está disponível.
Caso ela esteja disponível, tentamos seta-la para True (falo em tentar seta-la pois ela pode perder a CPU para uma outra Thread que veja que o get está definido com valor False).
Deve-se usar quando a concorrência é alta para um número alto de Threads. Pois, quando usamos TAS, esse tipo de implementação para exclusão mútua pode fazer a CPU descartar o valor armazenado da memória cache e assim, quando a Thread tentar ler, a memória cache irá dar cache miss para buscar na memória RAM enquanto o processo é bloqueado aguardando e que por sua vez gasta mais ciclos de CPU.

Petterson é usado para apenas 2 Threads. Ela garante que haja um controle alternado entre duas Threads que queiram usar a região crítica. 

Bakery é usado quando temos um número grande de Threads querendo entrar na região crítica que usam um tempo curto e quando necessariamente queremos implementar uma execução justa das Thread em forma de fila por ordem de chegada. Assim, uma Thread que executa uma região crítica não pode furar a fila das Threads que tem bilhetes menores que ele. 
