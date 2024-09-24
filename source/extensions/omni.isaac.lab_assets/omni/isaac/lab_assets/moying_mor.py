import omni.isaac.lab.sim as sim_utils
from omni.isaac.lab.actuators import ActuatorNetLSTMCfg, DCMotorCfg
from omni.isaac.lab.actuators import ImplicitActuatorCfg
from omni.isaac.lab.assets.articulation import ArticulationCfg
from omni.isaac.lab.sensors import RayCasterCfg
from omni.isaac.lab.utils.assets import ISAACLAB_NUCLEUS_DIR
path = "/home/jk/Project/HumanoidLearning/IsaacLab/source/extensions/omni.isaac.lab_assets/data"
MOYING_MOR_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=path+"/Robots/Moying/moying_mor.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "elfin_joint1": 0.5,
            "elfin_joint2": -0.6,
            "elfin_joint3": 0.0,
            "elfin_joint4": 0.0,
            "elfin_joint5": -1.0,
            "elfin_joint6": 0.0,
            "forward_left_wheel_joint": 0.0,
            "forward_right_wheel_joint": 0.0,
            "back_left_wheel_joint": 0.0,
            "back_right_wheel_joint": 0.0,
            "finger_joint": 0.70,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=[".*_joint[1-7]"],
            velocity_limit=100.0,
            effort_limit={
                ".*_joint[1-2]": 100.0,
                ".*_joint[3-4]": 50.0,
                ".*_joint[5-7]": 30.0,
            },
            stiffness={
                ".*_joint[1-4]": 2000.0,
                ".*_joint[5-7]": 2000.0,
            },
            damping={
                ".*_joint[1-4]": 0.0,
                ".*_joint[5-7]": 0.0,
            },
        ),
        "wheel": ImplicitActuatorCfg(
            joint_names_expr=[".*_wheel_joint"],
            velocity_limit=20.0,
            effort_limit=0.0,
            stiffness=0.0,
            damping=0.0,
        ),
        "gripper": ImplicitActuatorCfg(
            joint_names_expr=["finger_joint"],
            velocity_limit=100.0,
            effort_limit=2.0,
            stiffness=100.2,
            damping=0.01,
        ),
        # "roller": ImplicitActuatorCfg(
        #     joint_names_expr=[".*_roller_[0-7]_joint"],
        #     velocity_limit=2.0,
        #     effort_limit=2.0,
        #     stiffness=0.0,
        #     damping=0.00,
        # ),
    },
)


MOYING_MCR_CFG = ArticulationCfg(
    spawn=sim_utils.UsdFileCfg(
        usd_path=path+"/Robots/Moying/moying_mcr.usd",
        rigid_props=sim_utils.RigidBodyPropertiesCfg(
            disable_gravity=False,
            max_depenetration_velocity=5.0,
        ),
        articulation_props=sim_utils.ArticulationRootPropertiesCfg(
            enabled_self_collisions=True, solver_position_iteration_count=8, solver_velocity_iteration_count=0
        ),
        activate_contact_sensors=False,
    ),
    init_state=ArticulationCfg.InitialStateCfg(
        joint_pos={
            "left_arm_elfin_joint1": 0.0,
            "left_arm_elfin_joint2": 0.0,
            "left_arm_elfin_joint3": 0.0,
            "left_arm_elfin_joint4": 0.0,
            "left_arm_elfin_joint5": 0.0,
            "left_arm_elfin_joint6": 0.0,
            "left_arm_robotiq_85_left_knuckle_joint": 0.0,

            "right_arm_elfin_joint1": 0.0,
            "right_arm_elfin_joint2": 0.0,
            "right_arm_elfin_joint3": 0.0,
            "right_arm_elfin_joint4": 0.0,
            "right_arm_elfin_joint5": 0.0,
            "right_arm_elfin_joint6": 0.0,
            "right_arm_robotiq_85_left_knuckle_joint": 0.0,

            "forward_left_wheel_joint": 0.0,
            "forward_right_wheel_joint": 0.0,
            "back_left_wheel_joint": 0.0,
            "back_right_wheel_joint": 0.0,

            "head_joint1":0.0,
            "head_joint2":0.0,
        },
    ),
    actuators={
        "arm": ImplicitActuatorCfg(
            joint_names_expr=[".*_joint[1-7]"],
            velocity_limit=100.0,
            effort_limit={
                ".*_joint[1-2]": 100.0,
                ".*_joint[3-4]": 100.0,
                ".*_joint[5-7]": 100.0,
            },
            stiffness={
                ".*_joint[1-4]": 2000.0,
                ".*_joint[5-7]": 2000.0,
            },
            damping={
                ".*_joint[1-4]": 1.0,
                ".*_joint[5-7]": 0.0,
            },
        ),
        "wheel": ImplicitActuatorCfg(
            joint_names_expr=[".*_wheel_joint"],
            velocity_limit=10.0,
            effort_limit=2.0,
            stiffness=0.0,
            damping=0.00,
        ),
        "gripper": ImplicitActuatorCfg(
            joint_names_expr=[".*_robotiq_85_left_knuckle_joint"],
            velocity_limit=100.0,
            effort_limit=2.0,
            stiffness=100.2,
            damping=0.01,
        ),
        # "roller": ImplicitActuatorCfg(
        #     joint_names_expr=[".*_roller_[0-7]_joint"],
        #     velocity_limit=2.0,
        #     effort_limit=2.0,
        #     stiffness=0.0,
        #     damping=0.0,
        # ),
    },
)