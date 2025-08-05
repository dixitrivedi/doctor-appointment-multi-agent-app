from app.toolkit.check_availability_by_doctor import check_availability_by_doctor
from app.toolkit.check_availability_by_specialization import check_availability_by_specialization
from app.toolkit.set_appointment import set_appointment
from app.toolkit.cancel_appointment import cancel_appointment
from app.toolkit.reschedule_appointment import reschedule_appointment

class AppointmentToolkit:
    """Central registry for all appointment-related tools"""
    
    # Individual tools
    availability_by_doctor = check_availability_by_doctor
    availability_by_specialization = check_availability_by_specialization
    set_appointment_tool = set_appointment
    cancel_appointment_tool = cancel_appointment
    reschedule_appointment_tool = reschedule_appointment
    
    # Grouped tools
    availability_tools = [
        check_availability_by_doctor,
        check_availability_by_specialization
    ]
    
    management_tools = [
        set_appointment,
        cancel_appointment,
        reschedule_appointment
    ]
    
    @classmethod
    def get_all_tools(cls):
        """Get all available tools"""
        return cls.availability_tools + cls.management_tools
    
    @classmethod
    def get_availability_tools(cls):
        """Get only availability checking tools"""
        return cls.availability_tools
    
    @classmethod
    def get_management_tools(cls):
        """Get only appointment management tools"""
        return cls.management_tools
    
    @classmethod
    def get_tool_by_name(cls, tool_name: str):
        """Get a specific tool by name"""
        tool_mapping = {
            'check_availability_by_doctor': cls.availability_by_doctor,
            'check_availability_by_specialization': cls.availability_by_specialization,
            'set_appointment': cls.set_appointment_tool,
            'cancel_appointment': cls.cancel_appointment_tool,
            'reschedule_appointment': cls.reschedule_appointment_tool
        }
        return tool_mapping.get(tool_name)

# Usage example
# if __name__ == "__main__":
#     toolkit = AppointmentToolkit()
    
#     # Get all tools
#     all_tools = toolkit.get_all_tools()
#     print(f"Total tools: {len(all_tools)}")
    
#     # Get specific tool
#     doctor_availability_tool = toolkit.get_tool_by_name('check_availability_by_doctor')
    
#     # Get tool categories
#     availability_tools = toolkit.get_availability_tools()
#     management_tools = toolkit.get_management_tools()
    
#     print(f"Availability tools:============>", availability_tools)
#     print(f"Management tools:", management_tools)