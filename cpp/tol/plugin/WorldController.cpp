//
// Created by elte on 6-6-15.
//

#include "WorldController.h"
#include <iostream>

namespace gz = gazebo;

namespace tol {

void WorldController::Load(gz::physics::WorldPtr world, sdf::ElementPtr /*_sdf*/) {
	std::cout << "World plugin loaded." << std::endl;

	// Store the world
	world_ = world;

	// Create transport node
	node_.reset(new gz::transport::Node());
	node_->Init();

	// Subscribe to insert request messages
	insertSub_ = node_->Subscribe("~/insert_robot_sdf/request",
								  &WorldController::InsertRequest, this);
}

void WorldController::InsertRequest(ConstInsertSdfRequestPtr &request) {
	std::cout << "Insert request! Inserting SDF..." << std::endl;

	sdf::SDF robotSDF;
	robotSDF.SetFromString(request->sdf_contents());
	world_->InsertModelSDF(robotSDF);

	std::cout << "Inserted SDF for " << request->robot_id() << std::endl;
}

}
