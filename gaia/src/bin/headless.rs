use gaia::core::solver::{PhysicsWorld, RigidBody};
use gaia::core::shapes::{Shape, PhysicsMaterial};
use macroquad::prelude::Vec3;
use serde::{Deserialize, Serialize};
use serde_json;
use std::io::{self, BufRead};
use std::sync::mpsc;
use std::thread;

#[derive(Deserialize, Debug)]
#[serde(tag = "command")]
enum InternalCommand {
    #[serde(rename = "apply_force")]
    ApplyForce {
        body_id: usize,
        force: [f32; 3],
    },
    #[serde(rename = "apply_impulse")]
    ApplyImpulse {
        body_id: usize,
        impulse: [f32; 3],
    },
    #[serde(rename = "stop")]
    Stop,
}

fn main() {
    let mut phys = PhysicsWorld::new();
    
    // 0. Static Floor
    let floor_mat = PhysicsMaterial { restitution: 0.3, friction_static: 0.7, friction_dynamic: 0.5, density: 0.0 };
    let mut floor_body = RigidBody::new(0, Shape::Box { half_extents: Vec3::new(20.0, 1.0, 20.0) }, Vec3::new(0.0, -1.0, 0.0), floor_mat);
    floor_body.inv_mass = 0.0;
    floor_body.inv_inertia = Vec3::ZERO;
    phys.add_body(floor_body);

    // 1. Heavy Base (Support)
    let heavy_mat = PhysicsMaterial { density: 5000.0, ..Default::default() };
    phys.add_body(RigidBody::new(1, Shape::Box { half_extents: Vec3::new(5.0, 0.5, 5.0) }, Vec3::new(0.0, 0.5, 0.0), heavy_mat));

    // 2. Mobile Sphere (Light)
    let light_mat = PhysicsMaterial { density: 100.0, restitution: 0.8, ..Default::default() };
    phys.add_body(RigidBody::new(2, Shape::Sphere { radius: 0.5 }, Vec3::new(0.0, 5.0, 0.0), light_mat));

    // 3. Unstable Pillar
    let pillar_mat = PhysicsMaterial { density: 500.0, ..Default::default() };
    phys.add_body(RigidBody::new(3, Shape::Box { half_extents: Vec3::new(0.2, 3.0, 0.2) }, Vec3::new(5.0, 3.0, 0.0), pillar_mat));

    // 4. Standard Cube
    let cube_mat = PhysicsMaterial::default();
    phys.add_body(RigidBody::new(4, Shape::Box { half_extents: Vec3::ONE }, Vec3::new(-5.0, 8.0, 0.0), cube_mat));

    let dt = 0.016_f32;
    
    let (tx, rx) = mpsc::channel();
    thread::spawn(move || {
        let stdin = io::stdin();
        for line in stdin.lock().lines() {
            if let Ok(l) = line {
                if let Ok(cmd) = serde_json::from_str::<InternalCommand>(&l) {
                    let _ = tx.send(cmd);
                }
            }
        }
    });

    println!("INFO: GAIA Headless Started (Phase A: Affordance Discovery)");

    loop {
        while let Ok(cmd) = rx.try_recv() {
            match cmd {
                InternalCommand::ApplyForce { body_id, force } => {
                    if let Some(body) = phys.bodies.get_mut(body_id) {
                        body.force += Vec3::from_array(force);
                        println!("LOG: Applied force {:?} to body {}", force, body_id);
                    }
                }
                InternalCommand::ApplyImpulse { body_id, impulse } => {
                    if let Some(body) = phys.bodies.get_mut(body_id) {
                        body.apply_impulse(Vec3::from_array(impulse), body.position);
                        println!("LOG: Applied impulse {:?} to body {}", impulse, body_id);
                    }
                }
                InternalCommand::Stop => {
                    println!("INFO: Stop signal received.");
                    return;
                }
            }
        }

        phys.step(dt);
        
        let state_json = serde_json::to_string(&phys.bodies).unwrap();
        println!("FRAME_DATA: {}", state_json);
        
        thread::sleep(std::time::Duration::from_millis(16));
    }
}
