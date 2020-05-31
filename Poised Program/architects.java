public class architects {
		//Fields
		String name ;
		String surname;
		String telephone_number;
		String email_address;
		String physical_address;
		String project_number;
		
		public architects(String name, String surname, String telephone_number, String email_address, String physical_address, String project_number) {
			this.name = name;
			this.surname = surname;
			this.telephone_number = telephone_number;
			this.email_address = email_address;
			this.physical_address = physical_address;
			this.project_number = project_number;
		}
		
		public String getName() {
			return name + " " + surname;
		}
		
		public String getContact() {
			String contact = "Telephone Number: " + telephone_number;
			contact += "\nEmail Address: " + email_address;
			contact += "\nPhysical Address: " + physical_address;
			
			return contact;
		}
		
		public String toString() {
			String output = "Name: " + name;
		      output += "\nSurname:" + surname;
		      output += "\nTelephone Number:" + telephone_number;
		      output += "\nEmail Address:" + email_address;
		      output += "\nPhysical Address: " + physical_address;
		      output += "\nProject number: " + project_number;
		   
		      return output;
			
		}
	
}
