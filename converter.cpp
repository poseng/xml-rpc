#include <iostream>
#include <stdio.h>
#include <fstream>
#include <jsoncpp/json/json.h>

using namespace std;
int main(int argc, char * argv[])
{
    string path_to_json_dir("Data/trajectories/traj1.json");
    ifstream ifs(path_to_json_dir);
    Json::Reader reader;
    Json::Value obj;
    reader.parse(ifs, obj);
    const Json::Value& traj = obj;
    for (int i = 0; i < traj.size(); i++)
    {
        printf("id: %d\tlng: %.7lf\tlat: %.7lf\tcofiance: %.7lf\n",
                traj[i]["id"].asUInt(),
                traj[i]["lng"].asFloat(),
                traj[i]["lat"].asFloat(),
                traj[i]["confiance"].asFloat());        
    }
}