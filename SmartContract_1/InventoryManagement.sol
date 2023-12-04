// SPDX-License-Identifier: GPL-3.0
pragma solidity ^0.8.17;

contract ClothingManufacture {
    enum Status { Pending, Accepted, Rejected }

    struct Manufacturer {
        address manufacturerAddress;
        string manufacturerName;
    }

    struct Batch {
        address producer;
        string sellerName;
        string companyName;
        string batchNumber;
        string quantity;
        string companyAddress;
        Status status;
    }

    Manufacturer public manufacturer;
    mapping(string => Batch) private batches;
    mapping(address => string[]) private producerBatches;

    modifier onlyManufacturer() {
        require(msg.sender == manufacturer.manufacturerAddress, "Only the manufacturer can call this function.");
        _;
    }

    constructor(string memory _manufacturerName) {
        manufacturer.manufacturerAddress = msg.sender;
        manufacturer.manufacturerName = _manufacturerName;
    }



    function createBatch(string memory _batchNumber, address _producer, string memory _sellerName, string memory _companyName, string memory _quantity, string memory _companyAddress) public onlyManufacturer {
        require(batches[_batchNumber].producer == address(0), "Batch with this number already exists.");
        Batch storage b = batches[_batchNumber];
        b.producer = _producer;
        b.sellerName = _sellerName;
        b.companyName = _companyName;
        b.batchNumber = _batchNumber;
        b.quantity = _quantity;
        b.companyAddress = _companyAddress;
        b.status = Status.Pending;

        producerBatches[_producer].push(_batchNumber);
    }

    function getBatches(address _producer) public view returns (string[] memory) {
        return producerBatches[_producer];
    }

    function verifyBatch(string memory _batchNumber) public view returns (address, string memory, string memory, string memory, string memory, string memory, string memory) {
        Batch memory b = batches[_batchNumber];
        string memory status;
        if (b.status == Status.Pending) {
            status = "Verification pending by the producer";
        } else if (b.status == Status.Accepted) {
            status = "Verification accepted by the producer";
        } else if (b.status == Status.Rejected) {
            status = "Verification rejected by the producer";
        }
        return (b.producer, b.sellerName, b.companyName, b.batchNumber, b.quantity, b.companyAddress, status);
    }

    function acceptBatch(string memory _batchNumber) public {
        require(batches[_batchNumber].producer == msg.sender, "Only the producer can accept the batch.");
        require(batches[_batchNumber].status == Status.Pending, "The batch must be in pending status.");
        batches[_batchNumber].status = Status.Accepted;
    }

    function rejectBatch(string memory _batchNumber) public {
        require(batches[_batchNumber].producer == msg.sender, "Only the producer can reject the batch.");
        require(batches[_batchNumber].status == Status.Pending, "The batch must be in pending status.");
        batches[_batchNumber].status = Status.Rejected;
    }
}
