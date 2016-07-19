import java.io.*;

public class main {
	public static void main(String [] args){
		try{
			File file = new File("/home/gdm1/바탕화면/LAPACKfunc.txt");
			FileReader fileReader = new FileReader(file);
			BufferedReader reader = new BufferedReader(fileReader);
			
			BufferedWriter writer = new BufferedWriter(new FileWriter("/home/gdm1/바탕화면/LAPACK.txt"));
			
			String line = null;
			int count = 2;
			
			String text = "";  //설명
			String parameter = "";
			String name = "";
			String prefix = "";
			
			int cv=0;
			
			while((line = reader.readLine()) != null){				
				if (line.length() > 2) {
					if (line.charAt(0) == '[') {
						
						prefix = line.substring(1,5);
						
						
						int n=8;
						for(int i = 7; i < line.length(); i++)
							if(line.charAt(i) == ' '){ n = i; break;}
						name = "_"+line.substring(7,n).toUpperCase();
						
						
						for(int i = n+1; i < line.length(); i++){
							if(line.charAt(i) != ' ' && line.charAt(i) != '(' ){
								
								if(line.charAt(i) == ')'){
									break;
								}
								
								if(line.charAt(i) == ','){
									parameter += "	";
									continue;
								}
							
								parameter += Character.toString(line.charAt(i));
								
							}
						}
						
						//write
						writer.write(parameter);
						writer.newLine();
						
						parameter = "";
					}else{
						text = line;
					}
				}
			}
			
			reader.close();
			writer.close();
		}catch(Exception ex){
			System.out.println(ex);
		}
	}
}
