public class main
{
   public static void main (String [] args)
   {
      projects starlight = new projects("P1Tes1","Starlight","Apartment Block","12 Fever Close, Montana","ERF21234",300000000 , 150000, "30 October 2021");
      contractors koffee = new contractors("Koffee","Kyle","0772123234","k.kyle@icloud.com","7 Salmine Road","P1Tes1");
      customers james = new customers("James","Gardner","0771223114","JamieJamesGAr@icloud.com","9 Accasia Close, Reverand","P1Tes1");
      architects miles = new architects("Miles", "Harmony","0877122395","milesharm@gmail.com","99 James harden drive","P1Tes1");
    
      System.out.println("Projects\n");
      System.out.println(starlight + "\n");
      
      System.out.println("Customers\n");
      System.out.println(james + "\n");
      
      System.out.println("Architects\n");
      System.out.println(miles + "\n");
           
      System.out.println("Contractors\n");
      System.out.println(koffee + "\n");
      
   }
}