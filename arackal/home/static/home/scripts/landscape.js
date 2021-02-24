import {MTLLoader} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/loaders/MTLLoader.js';
import {OBJLoader2} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/loaders/OBJLoader2.js';
import {MtlObjBridge} from 'https://threejsfundamentals.org/threejs/resources/threejs/r122/examples/jsm/loaders/obj2/bridge/MtlObjBridge.js';


function main() {
    const canvas = document.querySelector('#c');
    const renderer = new THREE.WebGLRenderer({canvas});

    const scene = new THREE.Scene();
    scene.background = new THREE.Color(0x7fe3e3)




    const fov = 45;
    const aspect = 2;  // the canvas default
    const near = 0.1;
    const far = 300;
    const camera = new THREE.PerspectiveCamera(fov, aspect, near, far);

    scene.add(camera);
    camera.position.set(-20.39732808127235, 8.491698579320456, 5.191119003284504);
    camera.lookAt(0,0,0)


    const light = new THREE.HemisphereLight( 0xffffbb, 0x080820, 1.5);
    scene.add( light );




    
    const mtlLoader = new MTLLoader();

    {
        mtlLoader.load("{% static 'home/models/pipe/pipe.mtl' %}", (mtlParseResult) => {
        const objLoader = new OBJLoader2();
        const materials =  MtlObjBridge.addMaterialsFromMtlLoader(mtlParseResult);
        objLoader.addMaterials(materials);
            objLoader.load("{% static 'home/models/pipe/pipe.obj' %}", (root) => {

                root.scale.set(1.5,1.5,1.5);
                scene.add(root);

            });
        });
    }


    const handleMesh = new THREE.Object3D();
    handleMesh.position.y -= 0.1;
    scene.add(handleMesh)
    {
        mtlLoader.load("{% static 'home/models/handle/handle.mtl' %}", (mtlParseResult) => {
        const objLoader = new OBJLoader2();
        const materials =  MtlObjBridge.addMaterialsFromMtlLoader(mtlParseResult);
        objLoader.addMaterials(materials);
            objLoader.load("{% static 'home/models/handle/handle.obj' %}", (root) => {

                root.scale.set(1.5,1.5,1.5);
                handleMesh.add(root);

            });
        });
    }

    


    const blockgeo = new THREE.BoxGeometry(30,30,40);
    const blockmat = new THREE.MeshPhongMaterial({color:0x63717d, vertexColors:THREE.FaceColors});
    const blockmesh = new THREE.Mesh(blockgeo, blockmat);
    blockmesh.geometry.faces[ 2 ].color.setHex( 0x4e5861 ); 
    blockmesh.geometry.faces[ 3 ].color.setHex( 0x4e5861 ); 

    blockmesh.position.set(12, -5.8, -24);

    scene.add(blockmesh)
    




    
    window.addEventListener("scroll", function(event){
        const pos = window.scrollY/3876
        console.log(pos)
        handleMesh.rotation.y = 4*Math.PI*pos

        if(pos > .3){
            $('.content').fadeOut(500);
        }else{
            $('.content').fadeIn(500);
        }

        if(pos > .3 && pos < .7){
            rotateCamera((pos-.3)*2.5)
        }

    });


    const finalPoint = new THREE.Vector3(7.57651299677906, 8.013077210166774, 20.944300585467776);
    const mPoint = new THREE.Vector3(-6.6, 8.013077210166774, 15);
    const startPoint = new THREE.Vector3(-20.39732808127235, 8.013077210166774, 5.191119003284504);
    const curve = new THREE.CatmullRomCurve3([startPoint, mPoint, finalPoint]);
    curve.tension = .05;
    function rotateCamera(t){
        camera.position.copy(curve.getPoint(t))
        camera.lookAt(0,0,0)


        if(t > .25){
            $('.request').fadeOut(500);
            $('.request-form').fadeOut(500);
            $('.license-number').fadeOut(500);
        }else{
            $('.request').fadeIn(500);
            $('.license-number').fadeIn(500);
        }

        if(t > .45){
            $('.contact').fadeIn(500);

        }else{
            $('.contact').fadeOut(500);
        }


        if(t > .75){
            $('.p0').fadeIn(500);

        }else{
            $('.p0').fadeOut(500);
        }

        if(t > .80){
            $('.p1').fadeIn(500);

        }else{
            $('.p1').fadeOut(500);
        }

        if(t > .85){
            $('.p2').fadeIn(500);

        }else{
            $('.p2').fadeOut(500);
        }

        if(t > .90){
            $('.p3').fadeIn(500);

        }else{
            $('.p3').fadeOut(500);
        }

    }
    



    function render(time){
        time *= 0.001;

        if(resizeRendererToDisplaYSize(renderer)){
            const canvas = renderer.domElement;
            camera.aspect = canvas.clientWidth / canvas.clientHeight;
            camera.updateProjectionMatrix();
        }


       
        renderer.render(scene, camera);
        requestAnimationFrame(render);
    }



    function resizeRendererToDisplaYSize(renderer) {
        const canvas = renderer.domElement;
        const pixelRatio = window.devicePixelRatio;
        const width = canvas.clientWidth * pixelRatio | 0;
        const height = canvas.clientHeight * pixelRatio | 0;
        const needResize = canvas.width !== width || canvas.height !== height;
        if (needResize){
            renderer.setSize(width, height, false);
        }
        return needResize;
    }

    requestAnimationFrame(render);

}

if(window.matchMedia("(max-width: 700px)")){
    main()
}

