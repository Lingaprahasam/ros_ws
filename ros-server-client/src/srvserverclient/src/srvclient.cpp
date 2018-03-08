#include "ros/ros.h"
#include "srvserver/srvcomm.h"

class MCClient
{
public:
  MCClient(ros::NodeHandle& nh)
    {
        mc_cllient_ = nh.serviceClient<srvserver::srvcomm>("mc_command");
    }

    void start(const std::string& init)
    {
        ROS_INFO("Attempting to initialize motor controller");        
        // mc command
        srvserver::srvcomm srv;

        // Using Parameter to request
        srv.request.command = init;
        ROS_INFO_STREAM("Requesting init of motor controller: " << init);

        if (!mc_cllient_.call(srv))
        {
            ROS_ERROR("Could not initialize motor controller");
            return;
        }
        ROS_INFO_STREAM("motor controller initialized: " << srv.response);
    }


private:
    // Planning components
    ros::ServiceClient mc_cllient_;
};

int main(int argc, char **argv)
{
    std::string init;

    ros::init(argc, argv, "srvserver");
    ros::NodeHandle nh;

    // Private Node Handle
    ros::NodeHandle private_node_handle ("~");

    // parameter name, string object reference, default value
    private_node_handle.param<std::string>("mc_command", init, "init"); 

    ROS_INFO("srvserver node has been initialized");

    MCClient app(nh);    

    ros::Duration(.5).sleep();  // wait for the class to initialize
    app.start(init);

    ros::spin();
}