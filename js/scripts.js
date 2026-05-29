function defaultStructureRepresentation( component ){
    // bail out if the component does not contain a structure
    if( component.type !== "structure" ) return;
    // add three representations
    component.addRepresentation( "cartoon", {
        aspectRatio: 3.0,
        scale: 1.5
    } );
    component.addRepresentation( "licorice", {
        sele: "hetero and not ( water or ion )",
        multipleBond: true
    } );
    component.addRepresentation( "spacefill", {
        sele: "water or ion",
        scale: 0.5
    } );
}
