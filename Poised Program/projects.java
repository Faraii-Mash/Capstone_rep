
public class projects {
	//Fields
		String project_number;
		String project_name;
		String building_type;
		String project_physical_address;
		String erf_number;
		int project_total_fee;
		int project_paid_fee;
		String project_deadline;
		
		public projects(String project_number, String project_name, String building_type, String project_physical_address, String erf_number, int project_total_fee, int project_paid_fee, String project_deadline) {
			this.project_number = project_number;
			this.project_name = project_name;
			this.building_type = building_type;
			this.project_physical_address = project_physical_address;
			this.erf_number = erf_number;
			this.project_total_fee = project_total_fee;
			this.project_paid_fee = project_paid_fee;
			this.project_deadline = project_deadline;
		}
		
		public String toString() {
			String output = "Project number; " + project_number;
			output += "\nProject name: " + project_name;
			output += "\nBuilding type: " + building_type; 
			output += "\nProject physical Address: " + project_physical_address;
			output += "ERF number; " + erf_number;
			output += "Total fee due: " + project_total_fee;
		    output += "Total amount paid to date: " + project_paid_fee;
		    output += "\nThis project is due on date: " + project_deadline;
		   
		      return output;
			
			
		}

}
