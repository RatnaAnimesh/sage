/// Phase 14: Collision Shapes
///
/// Every rigid body is assigned a `Shape`. The `support()` function (farthest point
/// along a direction) is used by the GJK algorithm for exact narrow-phase collision.

use macroquad::prelude::Vec3;

use serde::{Deserialize, Serialize};

pub mod ser_vec3 {
    use super::Vec3;
    use serde::{Deserializer, Serializer};
    use serde::de::{SeqAccess, Visitor};
    use std::fmt;

    pub fn serialize<S>(v: &Vec3, serializer: S) -> Result<S::Ok, S::Error>
    where
        S: Serializer,
    {
        use serde::ser::SerializeSeq;
        let mut seq = serializer.serialize_seq(Some(3))?;
        seq.serialize_element(&v.x)?;
        seq.serialize_element(&v.y)?;
        seq.serialize_element(&v.z)?;
        seq.end()
    }

    pub fn deserialize<'de, D>(deserializer: D) -> Result<Vec3, D::Error>
    where
        D: Deserializer<'de>,
    {
        struct Vec3Visitor;

        impl<'de> Visitor<'de> for Vec3Visitor {
            type Value = Vec3;

            fn expecting(&self, formatter: &mut fmt::Formatter) -> fmt::Result {
                formatter.write_str("a sequence of 3 floats")
            }

            fn visit_seq<V>(self, mut seq: V) -> Result<Vec3, V::Error>
            where
                V: SeqAccess<'de>,
            {
                let x = seq.next_element()?.ok_or_else(|| serde::de::Error::invalid_length(0, &self))?;
                let y = seq.next_element()?.ok_or_else(|| serde::de::Error::invalid_length(1, &self))?;
                let z = seq.next_element()?.ok_or_else(|| serde::de::Error::invalid_length(2, &self))?;
                Ok(Vec3::new(x, y, z))
            }
        }

        deserializer.deserialize_seq(Vec3Visitor)
    }
}

/// A physics material controlling contact response
#[derive(Clone, Debug, Serialize, Deserialize)]
pub struct PhysicsMaterial {
    pub restitution: f32,       // Bounciness [0..1]
    pub friction_static: f32,   // Static friction coefficient
    pub friction_dynamic: f32,  // Kinetic friction coefficient
    pub density: f32,           // kg/m
}

impl Default for PhysicsMaterial {
    fn default() -> Self {
        Self { restitution: 0.3, friction_static: 0.6, friction_dynamic: 0.4, density: 1000.0 }
    }
}

/// All supported collision shapes
#[derive(Clone, Debug, Serialize, Deserialize)]
#[serde(tag = "type")]
pub enum Shape {
    Sphere { radius: f32 },
    Box    { 
        #[serde(with = "ser_vec3")]
        half_extents: Vec3 
    },
    Capsule { radius: f32, half_height: f32 },
}

impl Shape {
    /// GJK support function: returns the farthest point in direction `dir`
    pub fn support(&self, local_dir: Vec3) -> Vec3 {
        match self {
            Shape::Sphere { radius } => {
                let len = local_dir.length();
                if len < 1e-6 { return Vec3::ZERO; }
                local_dir / len * (*radius)
            }
            Shape::Box { half_extents } => {
                Vec3::new(
                    if local_dir.x >= 0.0 {  half_extents.x } else { -half_extents.x },
                    if local_dir.y >= 0.0 {  half_extents.y } else { -half_extents.y },
                    if local_dir.z >= 0.0 {  half_extents.z } else { -half_extents.z },
                )
            }
            Shape::Capsule { radius, half_height } => {
                // Support = hemisphere + cylinder core
                let mut p = Vec3::ZERO;
                p.y = if local_dir.y >= 0.0 { *half_height } else { -*half_height };
                let lateral = Vec3::new(local_dir.x, 0.0, local_dir.z);
                let lat_len = lateral.length();
                if lat_len > 1e-6 {
                    p += lateral / lat_len * (*radius);
                }
                p
            }
        }
    }

    /// Compute mass and inertia tensor for a given density
    pub fn mass_properties(&self, material: &PhysicsMaterial) -> (f32, Vec3) {
        match self {
            Shape::Sphere { radius } => {
                let mass = material.density * (4.0 / 3.0) * std::f32::consts::PI * radius.powi(3);
                let i    = 0.4 * mass * radius * radius;
                (mass, Vec3::new(i, i, i))
            }
            Shape::Box { half_extents } => {
                let (a, b, c) = (half_extents.x * 2.0, half_extents.y * 2.0, half_extents.z * 2.0);
                let mass = material.density * a * b * c;
                let ix = mass / 12.0 * (b * b + c * c);
                let iy = mass / 12.0 * (a * a + c * c);
                let iz = mass / 12.0 * (a * a + b * b);
                (mass, Vec3::new(ix, iy, iz))
            }
            Shape::Capsule { radius, half_height } => {
                let cyl_mass   = material.density * std::f32::consts::PI * radius * radius * half_height * 2.0;
                let sph_mass   = material.density * (4.0 / 3.0) * std::f32::consts::PI * radius.powi(3);
                let mass = cyl_mass + sph_mass;
                let iy = (cyl_mass * radius * radius / 2.0) + (2.0 * sph_mass * radius * radius / 5.0);
                let ix = (cyl_mass * (3.0 * radius * radius + (half_height * 2.0).powi(2)) / 12.0)
                       + (sph_mass * (2.0 * radius * radius / 5.0 + half_height * half_height));
                (mass, Vec3::new(ix, iy, ix))
            }
        }
    }
}
