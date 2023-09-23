import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
import java.util.concurrent.Semaphore;

public class WordCountConc {

    public static int WC = 0;

    public static Semaphore mutex= new Semaphore(1);

    public static void main(String[] args) throws InterruptedException {

        if (args.length != 1) {
            System.err.println("Usage: java WordCount <root_directory>");
            System.exit(1);
        }

        String rootPath = args[0];
        File rootDir = new File(rootPath);
        File[] subdirs = rootDir.listFiles();
        int numThreads = 0;

        for (File subdir : subdirs) {
            if (subdir.isDirectory()) {
                numThreads++;
            }
        }

        Thread[] threads = new Thread[numThreads];

        if (subdirs != null) {
            int pos = 0;
            for (File subdir : subdirs) {
                if (subdir.isDirectory()) {
                    String dirPath = rootPath + "/" + subdir.getName();
                    MyFunc run = new MyFunc(dirPath);
                    Thread t = new Thread(run);
                    threads[pos] = t;
                    t.start();
                }
                pos++;
            }

            for(Thread t : threads) {
                if(t != null){
                    t.join();
                }
            }
        }
        System.out.println(WC);
    }

    static class MyFunc implements Runnable {

        String dirpath;

        MyFunc(String dirpath) {this.dirpath = dirpath;}

        public void run() {
            try{
                wcDir(dirpath);
            }catch(Exception e){
                e.printStackTrace();
            }
        }

        private int wc(String fileContent) {
            String[] words = fileContent.split("\\s+");
            return words.length;
        }

        private int wcFile(String filePath) {
            try {
                BufferedReader reader = new BufferedReader(new FileReader(filePath));
                StringBuilder fileContent = new StringBuilder();
                String line;

                while ((line = reader.readLine()) != null) {
                    fileContent.append(line).append("\n");
                }

                reader.close();
                return wc(fileContent.toString());

            } catch (IOException e) {
                e.printStackTrace();
                return -1;
            }
        }

        private void wcDir(String dirPath) throws InterruptedException {
            File dir = new File(dirPath);
            File[] files = dir.listFiles();

            int count = 0;

            if (files != null) {
                for (File file : files) {
                    if (file.isFile()){
                        count += wcFile(file.getAbsolutePath());
                    }
                }
            }

            mutex.acquire();
            try{
                WC += count;
            } finally {
                mutex.release();
            }
        }

    }

}
